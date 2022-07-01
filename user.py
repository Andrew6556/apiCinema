from read_write_json import write_json_file, read_json_file
from path_file import PATH_JSON_REGISTRATION, PATH_INFO_USERS
from exceptions import*

import os
import json

def file_content(path_json: str):
    if os.stat(f'data/{path_json}').st_size:
        data: json = read_json_file(path_json)
    else:
        data: dict = {}
    return data




class User:

    @staticmethod
    def authenticate(name: str, password: int) -> object:
        try:
            user_hash = read_json_file(PATH_JSON_REGISTRATION)[name]
        except KeyError:
            raise UserNameDoesNotExist
        
        if user_hash["password"] == password:
            return User(name, password)

        raise PasswordError

    def __init__(self, name: str, password: int) -> None:
        self.username = name
        self.password = password

    def _basic_user_data(sefl):
        data = file_content(PATH_INFO_USERS)

        data.update({
            sefl.username:{
                "watched movie":[],
                "watch later":[]
                }})

        write_json_file(PATH_INFO_USERS, data)

    def checking_for_password_complexity(func):
        """Проверяем на сложность пароль"""
        def wrapper(self):
            if len(str(self.password)) < 8:
                raise IncorrectPasswordEntry
            return func(self)
        return wrapper

    def checking_for_correct_login(fucn):
        """Проверяем логин на корректность!
            без цифр, и должен начинаться с @
        """
        def wrapper(self):
            if list(filter(lambda letter:letter.isdigit(), self.username)):
                raise IncorrectLoginNumbers    
            elif not self.username.startswith('@'):
                raise LoginStartsWithNoCharacters
            return fucn(self)
        return wrapper

    @checking_for_password_complexity
    @checking_for_correct_login
    def user_registration(self):
        data = file_content(PATH_JSON_REGISTRATION)

        data.update({
            self.username:{
                "password":self.password,
                }
                })
        write_json_file(PATH_JSON_REGISTRATION, data)
        self._basic_user_data()

    def add_viewed_to_profile(self, watched_movie: str):
        """Добавление просмотренного фильма"""
        data = file_content(PATH_INFO_USERS)

        for user, data_us in data.items():
            if user == self.username:
                data_us["watched movie"].append(watched_movie)
                break
                
        write_json_file(PATH_INFO_USERS, data)

    def adding_a_movie_for_further_viewing(self, movie_later: str):
        """Сохраняем фильм на просмотр Позже"""
        data = file_content(PATH_INFO_USERS)

        for user, data_us in data.items():
            if user == self.username:
                data_us["watch later"].append(movie_later)
                break

        write_json_file(PATH_INFO_USERS, data)
    

    def check_for_valid_input_range_of_score(func):
        def wrapper(sefl, film, ball, genre_movie):
            if ball > 10:
                raise Overestimation
            elif ball < 0:
                raise Score_Below_Acceptable
            return func(sefl, film, ball, genre_movie)
        return wrapper

    @check_for_valid_input_range_of_score
    def movie_user_rating(sefl, film: str, ball: int, genre_movie: list):
        data = file_content(PATH_INFO_USERS)
        for key_hash, data_info in data[sefl.username].items():
            if key_hash == "user rating":
                data_info['films'].append({film:{
                                        "genres":genre_movie,
                                        "rating": ball}
                                        })
                break
        else:
            data[sefl.username].update({"user rating":
                                            {"films":[
                                                {film:{
                                                "genres":genre_movie,
                                                "rating": ball
                                                    }}
                                                ]}
                                        })
        write_json_file(PATH_INFO_USERS, data)

