from films_controller import FilmsController
from concol_film import Interface_Films
from user_interface import UserInterface
from user import User
from iter_page import IterPage
from operator import itemgetter
from exceptions import*


from path_file import PATH_JSON_FILMS, PATH_INFO_USERS
from read_write_json import read_json_file, write_json_file
from user import file_content
from check_json_movies import check_json_movies

import inspect
import operator



check_json_movies()


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

while True:
    print("""
        1.Можете добавлять в профиль просмотренные
        (нажав сюда, вы также можете вывести все просмотренные фильмы)
        2.Добавить фильмы в профиль, которые вы хотите посмотреть потом
        3.Выставить свои отметки фильмам 
        (в дальнейшим фильмы можно вывести по рейтингу)
    """)

    choice_user: int = int(input('введите,что выбрали(цифру): '))

    if choice_user == 1:
        films = FilmsController(read_json_file(PATH_JSON_FILMS))

        consol_films = Interface_Films(films)

        while True:
            movie_title: str = input('Напишите название просмотренного фильма\n')
            try:
                films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)
            except MovieNotfound:
                consol_films.output_of_found_films(movie_title)
            else:
                consol_films.output_of_found_films(movie_title)
                break

        while True:
            try:
                choice_watched_movie: int = int(input("Выберете,что из этого смотрели(введите цифру): "))
                user.add_viewed_to_profile(
                    films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)[choice_watched_movie]
                    )
            except KeyError:
                print('Введена недопустимая цифра вводе')
            else:
                print("Вы успешно добавили фильм!")
                choice_display_watched_movies = input(inspect.cleandoc("""
                                                    Вы хотите посмотреть все просмотренные фильмы в вашем профиле?
                                                    Напишите,Да или Нет: """))
                if choice_display_watched_movies.title() in ['Да',"Yes"]:
                    print("Просмотренные фильмы:")
                    consol_films.display_watched_movies(user_name)
                break
                
    elif choice_user == 2:
        films = FilmsController(read_json_file(PATH_JSON_FILMS))

        consol_films = Interface_Films(films)
        while True:
            movie_title: str = input('Напишите название фильма: ')
            try:
                films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)
            except MovieNotfound:
                consol_films.output_of_found_films(movie_title)
            else:
                consol_films.output_of_found_films(movie_title)
                break

        while True:
            try:
                choice_watched_movie: int = int(input("Выберете,что из этого смотрели(введите цифру): "))
                user.adding_a_movie_for_further_viewing(
                    films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)[choice_watched_movie]
                    )
            except KeyError:
                print('Введена недопустимая цифра вводе')
            else:
                print("Вы успешно добавили фильм!")
                break

    elif choice_user == 3:
        while True:
            user_consol = UserInterface(user)

            films = FilmsController(read_json_file(PATH_JSON_FILMS))
            consol_films = Interface_Films(films)
            print(""" 
                1. Добавить свою оценку фильму
                2. Вывести фильмы по рейтингу
                    Дальнейшие возможности:
                        1. От лучшего к худшему
                        2. От худшего к лучшему
                3. Вывод фильмов определённого жанра
                4. Расширенный функционал
                5. Выход из данного меню
            """)
            action_choice = int(input("Ваш выбор(напишите цифру): "))
            if action_choice == 1:
                while True:
                    movie_title: str = input('Напишите название фильма: ')
                    try:
                        films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)
                    except MovieNotfound:
                        consol_films.output_of_found_films(movie_title)
                    else:
                        consol_films.output_of_found_films(movie_title)
                        break

                loop_score = True
                while loop_score:
                    try:
                        choice_watched_movie: int = int(input("Выберете фильм(введите цифру): "))
                        film = films.a_set_of_occurrences_based_on_a_misspelled_film(movie_title)[choice_watched_movie]
                    except KeyError:
                        print('Введена недопустимая цифра вводе')
                    else:
                        while loop_score:
                            try:
                                film_score = int(input("Оцените данный фильм от 0 до 10: "))
                                user.movie_user_rating(film, film_score, films.film_genres(film))
                            except Overestimation:
                                user_consol.wrong_movie_rating(film, film_score, films.film_genres(film))
                            except ScoreBelowAcceptable:
                                user_consol.wrong_movie_rating(film, film_score, films.film_genres(film))
                            else:
                                print("Вы успешно добавили фильм!")
                                loop_score = False
            elif action_choice == 2:
                print(""" 
                    По какому каритерию хотите вывести фильмы:
                        1. От лучшего к худшему
                        2. От худшего к лучшему
                """)
                    
                movie_output_selection = int(input("Напишите цифру того ,что выбрали\n"))

                if movie_output_selection == 1:
                    print("Вывод:")
                    consol_films.output_of_evaluation_films_by_rating(True)

                elif movie_output_selection == 2:
                    print("Вывод:")
                    consol_films.output_of_evaluation_films_by_rating(False)
                else:
                    print("erorr")

            elif action_choice == 3:
                while True:
                    try:
                        choice_genre = input("Напишите жанр: ")
                        films.listing_specific_movies_by_genre(user_name, choice_genre)
                    except WrongGenre:
                        consol_films.output_of_films_depending_on_the_genre(user_name, choice_genre)
                    else:
                        print("Фильмы:")
                        consol_films.output_of_films_depending_on_the_genre(user_name, choice_genre)
                        break
            elif action_choice == 4:
                while True:
                    print("""
                        Добро пожаловать в Демо Кинопоиск
                        1.Поиск фильма по названию
                        2.Нахождение фильма по интересующему вас жанру
                        3.Выйти с данного меню        
                        """)


                    choice_user = int(input('Что вы хотите сделать(напишите цифрой): ')) 

                    if choice_user == 1:
                        films = FilmsController(read_json_file(PATH_JSON_FILMS))
                        consol_films = Interface_Films(films)

                        user_movie: str = input('Введите название фильма\n')
                        consol_films.concol_sorted_output_of_the_requested_movie_year(user_movie)


                    elif choice_user == 2:

                        loop: bool = True
                        while loop:
                            user_genre = input('Введите название жанра\n')
                            films = FilmsController(read_json_file(PATH_JSON_FILMS))
                            iter_page = IterPage(films.search_movies_by_genre_sorted_rating(user_genre))

                            try:
                                consol_films = Interface_Films(next(iter_page))
                            except StopIteration:
                                print("Вы ввели не существующий жанр")
                            else:
                                loop: bool = False

                        print('\nФильмы:')
                        consol_films.output_search_movies_by_genre_sorted_rating()
                        if len(iter_page.films) > 1:
                            print(f'{iter_page.current_page} из {iter_page.count_page} страница\n')
                            while True:
                                if iter_page.current_page == 1:
                                    print(inspect.cleandoc("""
                                            1. Сдедующая
                                            2. Выход"""))
                                
                                    choice_page_next = int(input("Введите цифру: "))
                                    if choice_page_next == 1:
                                        try:
                                            consol_films = Interface_Films(next(iter_page))
                                        except StopIteration:
                                            print("Больше фильмов данного жанра нету")
                                        else:
                                            consol_films.output_search_movies_by_genre_sorted_rating()
                                    else:
                                        print("Вы успешно вышли")
                                        break

                                elif iter_page.current_page > 1 and iter_page.current_page < iter_page.count_page:
                                    print(inspect.cleandoc("""
                                        1. Сдедующая
                                        2. Предыдущая
                                        3. Выход"""))
                                    choice_page = int(input("Введите цифру: "))
                                    if choice_page == 1:
                                        try:
                                            consol_films = Interface_Films(next(iter_page))
                                        except StopIteration:
                                            print("Больше фильмов данного жанра нету")
                                        else:
                                            consol_films.output_search_movies_by_genre_sorted_rating()

                                    elif choice_page == 2:
                                        try:
                                            consol_films = Interface_Films(iter_page.previous())
                                        except StopIteration:
                                            print("Больше фильмов данного жанра нету")
                                        else:
                                            consol_films.output_search_movies_by_genre_sorted_rating()
                                    else:
                                        print("Вы успешно вышли")
                                        break

                                elif iter_page.current_page == iter_page.count_page:
                                    print(inspect.cleandoc("""
                                            1. Предыдущая
                                            2. Выход"""))
                                    choice_page = int(input("Введите цифру: "))
                                    if choice_page == 1:
                                        try:
                                            consol_films = Interface_Films(iter_page.previous())
                                        except StopIteration:
                                            print("Больше фильмов данного жанра нету")
                                        else:
                                            consol_films.output_search_movies_by_genre_sorted_rating()
                                    else:
                                        print("Вы успешно вышли")
                                        break
                                
                                print(f'{iter_page.current_page} из {iter_page.count_page} страница\n')
                    elif choice_user == 3:
                        print("Вы успешно вышли")
                        break
                    else:
                        print('вы ввели несуществующее действие')
            elif action_choice == 5:
                print("Вы успешно вышли из программы")
                break


