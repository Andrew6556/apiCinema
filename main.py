from films_controller import FilmsController
from path_file import PATH_JSON_FILMS
from read_write_json import read_json_file
from concol_film import Interface_Films
from user_interface import UserInterface
from user import User
from iter_page import IterPage
from exceptions import*

import inspect



# if not os.stat(f'data/{PATH_JSON_FILMS}').st_size:
#     for number in range(1, all_pages_films("pagesCount") + 1):
#         data = read_json_file(PATH_JSON_FILMS)
#         data.append(all_pages_films("films", number))
#         write_json_file(PATH_JSON_FILMS, data)


loop: bool = True
while loop:
    user_choice: int = int(input("\
                \nЧто вы хотите сделать:\
                \n1.Зарегистрироваться\
                \n2.Войти\
                \nВаш выбор: "))

    if user_choice == 1:
        while True:
            user_name = input('Введите ваше имя\n')
            user_password = int(input('Введите пароль\n'))
            
            user = User(user_name, user_password)
            console = UserInterface(user)

            try:
                user.user_registration()
            except IncorrectLoginNumbers:
                console.error_message_in_login()
            except LoginStartsWithNoCharacters:
                console.error_message_in_login()
            except IncorrectPasswordEntry:
                console.correct_password_processing()
            else:
                break
        print('Регистрация прошла успешно')

    elif user_choice == 2:
        while loop:
            user_name = input('Введите ваше имя\n')
            user_password = int(input('Введите пароль\n'))

            try:
                user = User.authenticate(user_name, user_password)
                user_int = UserInterface(user)
            except UserNameDoesNotExist:
                print('Такого имени не существует в базе')
            except PasswordError:
                print('Неверный пароль!')
            else:
                loop = False
    else:
        print('Вы ввели не корректное действие')




















# print("""
#     Добро пожаловать в Демо Кинопоиск
#     1.Поиск фильма по названию
#     2.Нахождение фильма по интересующему вас жанру        
#     """)


# choice_user = int(input('Что вы хотите сделать(напишите цифрой): ')) 

# if choice_user == 1:
#     films = FilmsController(read_json_file(PATH_JSON_FILMS))
#     consol_films = Interface_Films(films)

#     user_movie: str = input('Введите название фильма\n')
#     consol_films.concol_sorted_output_of_the_requested_movie_year(user_movie)


# elif choice_user == 2:
#     loop: bool = True
#     while loop:
#         user_genre = input('Введите название жанра\n')
#         films = FilmsController(read_json_file(PATH_JSON_FILMS))
#         iter_page = IterPage(films.search_movies_by_genre_sorted_rating(user_genre))

#         try:
#             consol_films = Interface_Films(next(iter_page))
#         except StopIteration:
#             print("Вы ввели не существующий жанр")
#         else:
#             loop: bool = False

#     print('\nФильмы:')
#     consol_films.output_search_movies_by_genre_sorted_rating()
#     if len(iter_page.films) > 1:
#         print(f'{iter_page.current_page} из {iter_page.count_page} страница\n')
#         while True:
#             if iter_page.current_page == 1:
#                 print(inspect.cleandoc("""
#                         1. Сдедующая
#                         2. Выход"""))
            
#                 choice_page_next = int(input("Введите цифру: "))
#                 if choice_page_next == 1:
#                     try:
#                         consol_films = Interface_Films(next(iter_page))
#                     except StopIteration:
#                         print("Больше фильмов данного жанра нету")
#                     else:
#                         consol_films.output_search_movies_by_genre_sorted_rating()
#                 else:
#                     print("Вы успешно вышли")
#                     break

#             elif iter_page.current_page > 1 and iter_page.current_page < iter_page.count_page:
#                 print(inspect.cleandoc("""
#                     1. Сдедующая
#                     2. Предыдущая
#                     3. Выход"""))
#                 choice_page = int(input("Введите цифру: "))
#                 if choice_page == 1:
#                     try:
#                         consol_films = Interface_Films(next(iter_page))
#                     except StopIteration:
#                         print("Больше фильмов данного жанра нету")
#                     else:
#                         consol_films.output_search_movies_by_genre_sorted_rating()

#                 elif choice_page == 2:
#                     try:
#                         consol_films = Interface_Films(iter_page.previous())
#                     except StopIteration:
#                         print("Больше фильмов данного жанра нету")
#                     else:
#                         consol_films.output_search_movies_by_genre_sorted_rating()
#                 else:
#                     print("Вы успешно вышли")
#                     break

#             elif iter_page.current_page == iter_page.count_page:
#                 print(inspect.cleandoc("""
#                         1. Предыдущая
#                         2. Выход"""))
#                 choice_page = int(input("Введите цифру: "))
#                 if choice_page == 1:
#                     try:
#                         consol_films = Interface_Films(iter_page.previous())
#                     except StopIteration:
#                         print("Больше фильмов данного жанра нету")
#                     else:
#                         consol_films.output_search_movies_by_genre_sorted_rating()
#                 else:
#                     print("Вы успешно вышли")
#                     break
            
#             print(f'{iter_page.current_page} из {iter_page.count_page} страница\n')
# else:
#     print('вы ввели несуществующее действие')




