from typing import List
from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file, write_json_file
# import re



class Film:

    def __init__(self, films: list) -> None:
        self.films = films
        # self.sorted_films = sorted_films


    def films_by_specific_genre(self, genre: str) -> List:
        films_to_genre: list = []
        for film_hash in self.films:
            for films in film_hash:
                if genre.lower() in [films["genres"][i]["genre"]\
                    for i in range(0 , len(films["genres"]))]:
                        films_to_genre.append(films["nameRu"])

        return films_to_genre        