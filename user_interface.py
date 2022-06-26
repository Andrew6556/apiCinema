from exceptions import*



class UserInterface:

    def __init__(self, user: object) -> None:
        self.user = user

    def correct_password_processing(self):
        try:
            self.user.user_registration()
        except IncorrectPasswordEntry:
            print('Ваш пароль должен содержать цифр 8')

    def error_message_in_login(self):
        try:
            self.user.user_registration()
        except IncorrectLoginNumbers:
            print('Ваш логин не должен содержать цифр')
        except LoginStartsWithNoCharacters:
            print('Ваш логин должен начинаться с "@"')

    def wrong_movie_rating(self, film, film_score, genres):
        try:
            self.user.movie_user_rating(film, film_score, genres)
        except Overestimation:
            print('Вы ввели число, больше допустимого!')
        except Score_Below_Acceptable:
            print('Вы ввели число, меньше допустимого!')

