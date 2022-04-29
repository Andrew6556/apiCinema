from film import Film
from read_write_json import read_json_file, write_json_file
from path_file import PATH_JSON_FILMS
from func_api import all_pages_films


number_of_pages = all_pages_films("pagesCount")

for number in range(1, number_of_pages + 1):
    data = read_json_file(PATH_JSON_FILMS)
    data.append(all_pages_films("films", number))
    write_json_file(PATH_JSON_FILMS, data)


# for film_hash in page.values():
    # film = Film(film_hash["films"][0])
    # films.append(film)

# for film in films:
#     print(f"{film}\n")
