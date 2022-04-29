from film import Film
from read_write_json import read_json_file, write_json_file
from path_file import API_KEY, URL_API ,PATH_JSON_FILMS
# from func_api import 
import requests


number_of_pages = requests.get(
    URL_API,
    headers={
        "Content-type": "application/json",
        "X-API-KEY": API_KEY
    }
).json()["pagesCount"]

# Получаем указаную страницу
def all_pages_films(pages):
    return requests.get(
    URL_API,
    params={"page": pages},
    headers={
        "Content-type": "application/json",
        "X-API-KEY": API_KEY
    }
).json()["films"]

for i in range(1, number_of_pages + 1):
    data = read_json_file(PATH_JSON_FILMS)
    data.append(all_pages_films(i))
    write_json_file(PATH_JSON_FILMS, data)


# for film_hash in page.values():
    # film = Film(film_hash["films"][0])
    # films.append(film)

# for film in films:
#     print(f"{film}\n")
