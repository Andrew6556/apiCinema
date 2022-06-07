from exceptions import MovieNotfound
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