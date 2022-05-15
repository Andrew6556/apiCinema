from film import Film
from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file
from func_api import all_pages_films
from concol_film import Interface_Films
from iter_page import IterPage

# if not os.stat(f'data/{PATH_JSON_FILMS}').st_size:
#     for number in range(1, all_pages_films("pagesCount") + 1):
#         data = read_json_file(PATH_JSON_FILMS)
#         data.append(all_pages_films("films", number))
#         write_json_file(PATH_JSON_FILMS, data)


print("""
    Добро пожаловать в Демо Кинопоиск
    1.Поиск фильма по названию
    2.Нахождение фильма по интересующему вас жанру        
    """)

films = Film(read_json_file(PATH_JSON_FILMS))

consol_films = Interface_Films(films)

# choice_user = int(input('Что вы хотите сделать(напишите цифрой): ')) 

# if choice_user == 1:
#     user_movie = input('введите название фильма\n')
#     consol_films.concol_sorted_output_of_the_requested_movie_year(user_movie)
# elif choice_user == 2:
#     user_genre = input('введите название фильма\n')
#     consol_films.output_search_movies_by_genre_sorted_by_rating(user_genre)
# else:
#     print('вы ввели несуществующее действие')



# consol_films.concol_sorted_output_of_the_requested_movie_year('Брат')

# iter_page = IterPage(films.search_movies_by_genre_sorted_by_rating('криминал'))
# print(iter_page.films)
# print(next(iter_page))