from film import Film
from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file, write_json_file
from func_api import all_pages_films
from iter_page import IterPage

# if not os.stat(f'data/{PATH_JSON_FILMS}').st_size:
#     for number in range(1, all_pages_films("pagesCount") + 1):
#         data = read_json_file(PATH_JSON_FILMS)
#         data.append(all_pages_films("films", number))
#         write_json_file(PATH_JSON_FILMS, data)

films = Film(read_json_file(PATH_JSON_FILMS))

films.search_movies_by_genre_sorted_by_rating('криминал')

# iter_page = IterPage(films.search_movies_by_genre_sorted_by_rating('криминал'))
# # print(next(iter_page))
# print(iter_page.films)

# a = []

# arr =  [
#         '1',  '2', 
#         '3',  '4', 
#         '5',  '6', 
#         '7',  '8', 
#         '9',  '10', 
#         '11', '12',
#         '13', '14',
#         '15', '16',
#         '17', '18',
#         '19', '20',
#         '21', ]

# for i in range(0, len(arr), 5):
#     a.append(arr[i:i + 5])

# print(a)