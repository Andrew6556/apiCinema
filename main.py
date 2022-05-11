from film import Film
from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file, write_json_file
from func_api import all_pages_films


# if not os.stat(f'data/{PATH_JSON_FILMS}').st_size:
#     for number in range(1, all_pages_films("pagesCount") + 1):
#         data = read_json_file(PATH_JSON_FILMS)
#         data.append(all_pages_films("films", number))
#         write_json_file(PATH_JSON_FILMS, data)

films = Film(read_json_file(PATH_JSON_FILMS))

films.sorted_output_of_the_requested_movie('властелин')