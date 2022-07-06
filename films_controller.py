from operator import itemgetter
from exceptions import MovieNotfound, WrongGenre
from read_write_json import read_json_file
from path_file import PATH_INFO_USERS

import re


class FilmsController:

    def __init__(self, films: list) -> None:
        self.films = films

    def check_correct_name_movie(func):
        def wrapper(self, movie, *args, **kwargs):
            result = func(self, movie, *args, **kwargs)
            if len(result) == 0:
                raise MovieNotfound
            return result
        return wrapper
    
    @check_correct_name_movie
    def a_set_of_occurrences_based_on_a_misspelled_film(self, movie) -> list:
        """Нахождение вариантов фильма,при неправильном его написание"""
        variants_movies: list = []

        for film_hash in self.films:
            for film in film_hash:
                if re.search(fr"\b{movie}\b",
                    film["nameRu"], flags=re.IGNORECASE):
                    variants_movies.append(film["nameRu"])

        return dict(enumerate(variants_movies, start=1))

    def films_by_specific_genre(self, genre: str) -> list:
        """список фильмов по жанру"""
        films_to_genre: list = []
        for film_hash in self.films:
            for films in film_hash:
                if genre.lower() in [films["genres"][i]["genre"]\
                    for i in range(0 , len(films["genres"]))]:
                        films_to_genre.append(films["nameRu"])

        return films_to_genre        

    def sorted_output_of_the_requested_movie_year(self, movie: str) -> list:
        """
            Нахождение конретного фильма и его продолжений
            Сортированных по году
        """
        found_movies = []

        for film_hash in self.films:
            for film in film_hash:
                if re.search(fr"\b{movie}\b",
                    film["nameRu"], flags=re.IGNORECASE):
                        found_movies.append({
                            "film":film["nameRu"],
                            "year":film["year"],
                            "rating":film["rating"]
                        })
        
        return sorted(found_movies, key=itemgetter("year"))
    
    def __pagination_of_movies(self, sort_film: list, films_to_genre: list) -> list:
        return [sort_film[i: i + 5] for i in range(0, len(films_to_genre), 5)]

    def search_movies_by_genre_sorted_rating(self, genre: str) -> list:
        """Вывод всех фильмов по конретному жанру отсортированных по рейтингу"""
        films_to_genre = []
        
        for film_hash in self.films:
            for film in film_hash:
                if genre.lower() in [film["genres"][i]["genre"]\
                    for i in range(0 , len(film["genres"]))]:
                        films_to_genre.append({
                            "film":film["nameRu"],
                            "year":film["year"],
                            "rating":film["rating"]
                            })
        return self.__pagination_of_movies(
                        sorted(films_to_genre, key=itemgetter("rating")), films_to_genre)

    def film_genres(self, movie: str):
        movie_genre = []
        for film_hash in self.films:
            for films in film_hash:
                if movie == films["nameRu"]:
                    movie_genre.extend([films["genres"][i]["genre"]\
                        for i in range(0 , len(films["genres"]))])
        return movie_genre

    
    def sort_film_user_by_rating(self, side) -> dict:
        dict_rating_user_film = {}
        for hash_films in read_json_file(PATH_INFO_USERS)["@a"]["user rating"]["films"]:
            for data_film in hash_films.values():
                if data_film["rating"] in dict_rating_user_film:
                    dict_rating_user_film[data_film["rating"]].append(hash_films)
                else:
                    dict_rating_user_film[data_film["rating"]] = [hash_films]
        return  self.rating_film_more_to_less(dict_rating_user_film, side)

    def rating_film_more_to_less(self, sort_rating, side: bool) -> dict:
        return dict(sorted(sort_rating.items(), key=lambda x: x[0], reverse=side))

    def checking_for_a_movie(func):
        def wrapper(self, movie, *args, **kwargs):
            result = func(self, movie, *args, **kwargs)
            if len(result) == 0:
                raise WrongGenre
            return result
        return wrapper

    @checking_for_a_movie
    def listing_specific_movies_by_genre(self, genre: str, list_films: list) -> list:
        list_genre_films = []
        for hash_films in list_films:
            for value in hash_films.values():
                if genre.lower() in [value["genres"][i]\
                    for i in range(0 , len(value["genres"]))]:
                    list_genre_films.append(hash_films)
        return list_genre_films