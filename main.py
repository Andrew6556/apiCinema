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


# arr =  [
#         'IMG_0023_475_30.tif', 'IMG_0023_550_20.tif', 
#         'IMG_0023_670_30.tif', 'IMG_0023_715_10.tif', 
#         'IMG_0023_840_20.tif', 'IMG_0024_475_30.tif', 
#         'IMG_0024_550_20.tif', 'IMG_0024_670_30.tif', 
#         'IMG_0024_715_10.tif', 'IMG_0024_840_20.tif', 
#         'IMG_0025_475_30.tif', 'IMG_0025_550_20.tif', 
#         'IMG_0025_670_30.tif', 'IMG_0025_715_10.tif', 
#         'IMG_0025_840_20.tif', 'IMG_0026_475_30.tif', 
#         'IMG_0026_550_20.tif', 'IMG_0026_670_30.tif', 
#         'IMG_0026_715_10.tif', 'IMG_0026_840_20.tif']
# for i in range(0, len(arr)):
#     print(arr[i:i + 5])
