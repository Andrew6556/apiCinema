class Interface_Films:
    def __init__(self, films) -> None:
        self.films = films

    def concol_sorted_output_of_the_requested_movie_year(self, movie: str):
        sorted_movie_year = self.films.sorted_output_of_the_requested_movie_year(movie)
        if sorted_movie_year:
            for film_hash in sorted_movie_year:
                print(f"{film_hash['film']} ({film_hash['year']}), {film_hash['rating']}")
        else:
            print('Вы ввели не существующий фильм')
        
    def output_search_movies_by_genre_sorted_rating(self):
        
        # if sorted_by_movie_rating:
            for sorted_films in self.films:
                print(f"{sorted_films['film']} ({sorted_films['year']}), {sorted_films['rating']}")
        # else:
        #     print('lose')