from operator import itemgetter
import re



class Film:

    def __init__(self, films: list) -> None:
        self.films = films

    def films_by_specific_genre(self, genre: str) -> list:
        films_to_genre: list = []
        for film_hash in self.films:
            for films in film_hash:
                if genre.lower() in [films["genres"][i]["genre"]\
                    for i in range(0 , len(films["genres"]))]:
                        films_to_genre.append(films["nameRu"])

        return films_to_genre        

    def sorted_output_of_the_requested_movie(self, movie: str) -> list:
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
        
    def search_movies_by_genre_sorted_by_rating(self, genre: str) -> list:
        """ """
        films_to_genre: list = []

        for film_hash in self.films:
            for film in film_hash:
                if genre.lower() in [film["genres"][i]["genre"]\
                    for i in range(0 , len(film["genres"]))]:
                        films_to_genre.append({
                            "film":film["nameRu"],
                            "year":film["year"],
                            "rating":film["rating"]
                            })
        return sorted(films_to_genre, key=itemgetter("rating"))
        # implemented: search for movies by genre with ordered output