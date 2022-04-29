from path_file import API_KEY, URL_API 
import requests



# Получаем указаную страницу
def all_pages_films(chapter: str, pages: int = 1):
    return requests.get(
    URL_API,
    params={"page": pages},
    headers={
        "Content-type": "application/json",
        "X-API-KEY": API_KEY
    }
).json()[chapter]
