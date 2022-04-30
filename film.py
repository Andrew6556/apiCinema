from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file, write_json_file

class Film:

    def get_all_films() -> object:
        list_films = []
        for list_film_hash in read_json_file(PATH_JSON_FILMS):
            for hash_films in list_film_hash:
                film = Film(hash_films)
                list_films.append(film)
        return list_films

    def __init__(self, film_hash):
        self.film_hash = film_hash
        self.title = film_hash["nameRu"]
        self.year = film_hash["year"]
        
    def __str__(self):
        return f"Название: {self.title}\nГод: {self.year}"

    def films_by_genre(self, genre: str):
        if genre in [self.film_hash["genres"][i]["genre"]\
                    for i in range(0 , len(self.film_hash["genres"]))]:
            print(self.film_hash["nameRu"])