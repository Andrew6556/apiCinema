class Interface_Films:
    def __init__(self, films):
        self.films = films

    def concol_sorted_output_of_the_requested_movie_year(self, movie: str):
        sorted_movie_year = self.films.sorted_output_of_the_requested_movie_year(movie)
        if sorted_movie_year:
            for film_hash in sorted_movie_year:
                print(f"{film_hash['film']} ({film_hash['year']}), {film_hash['rating']}")
        else:
            print('Вы ввели не существующий фильм')
        
    def output_search_movies_by_genre_sorted_by_rating(self, genre: str):
        sorted_by_movie_rating = self.films.search_movies_by_genre_sorted_by_rating(genre)
        if sorted_by_movie_rating:
            for i in sorted_by_movie_rating:
                print(i)
        else:
            print('lose')