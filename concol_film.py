from exceptions import MovieNotfound,WrongGenre
from read_write_json import read_json_file
from path_file import PATH_INFO_USERS

import emoji
import inspect



class Interface_Films:
    def __init__(self, films) -> None:
        self.films = films

    def concol_sorted_output_of_the_requested_movie_year(self, movie: str):
        sorted_movie_year = self.films.sorted_output_of_the_requested_movie_year(movie)
        if sorted_movie_year:
            for film_hash in sorted_movie_year:
                print(emoji.emojize(f"{film_hash['film']} ({film_hash['year']}),:star: {film_hash['rating']}"))
        else:
            print('Вы ввели не существующий фильм')
        
    def output_search_movies_by_genre_sorted_rating(self):
        for sorted_films in self.films:
            print(emoji.emojize(inspect.cleandoc(f"{sorted_films['film']}({sorted_films['year']}),:star: {sorted_films['rating']}")))
        
    def output_of_found_films(self, movie: str):
        try:
            result = self.films.a_set_of_occurrences_based_on_a_misspelled_film(movie)
        except MovieNotfound:
            print("видимо, вы ввели фильма которого нету")
        else:
            for num, film in result.items():
                print(f"{num}. {film}")

    def display_watched_movies(sefl, name):
        for data_info in read_json_file(PATH_INFO_USERS)[name].values():
            for index, movies_watched in enumerate(data_info, start=1):
                print(f"{index}. {movies_watched}")

    def output_of_evaluation_films_by_rating(self, side: bool):
        result = self.films.sort_film_user_by_rating(side)
        
        for num, data_name in result.items():
            for hash in data_name:
                for name in hash:
                    print(f"{name} -- рейтинг фильма: {hash[name]['rating']} ")

    def output_of_films_depending_on_the_genre(self, username, genre: str):
        try:
            result = self.films.listing_specific_movies_by_genre(username, genre)
        except WrongGenre:
            print("error!Фильмов с этим жанром не найденно")
        else:
            for data_name in result:
                for i in data_name:
                    print(f"{i}")





            

