from read_write_json import write_json_file, read_json_file
from path_file import PATH_JSON_REGISTRATION

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
            return User(name, password, user_hash, True)

        raise PasswordError

    def __init__(self, name: str, password: int,
                    authenticate=False) -> None:

        self.username = name
        self.password = password
        self.is_authenticate = authenticate

    def registration(self):
        if os.stat(f'data/{PATH_JSON_REGISTRATION}').st_size:
            data = read_json_file(PATH_JSON_REGISTRATION)
        else:
            data = {}

        data.update({
            self.username:{
                "password":self.password,
                }})
        write_json_file(PATH_JSON_REGISTRATION, data)