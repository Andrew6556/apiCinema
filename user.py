import json
from read_write_json import write_json_file, read_json_file
from path_file import PATH_JSON_REGISTRATION, PATH_INFO_USERS

import os
from exceptions import*

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

        if os.stat(f'data/{PATH_JSON_REGISTRATION}').st_size:
            data = read_json_file(PATH_JSON_REGISTRATION)
        else:
            data = {}

        data.update({
            self.username:{
                "password":self.password,
                }
                })
        write_json_file(PATH_JSON_REGISTRATION, data)

    def add_viewed_to_profile(self, watched_movie: str):
        if os.stat(f'data/{PATH_INFO_USERS}').st_size:
            data: json = read_json_file(PATH_INFO_USERS)
        else:
            data: dict = {}

        data.update({
            self.username:{
                "watched movie": watched_movie
                }
            })

        write_json_file(PATH_INFO_USERS, data)