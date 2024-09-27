import os
import platform

import python_developer.Sequences_Strings_lists_sets_dictionaries.victory as victory_game
import python_developer.repo.lesson4_functions_dz.use_functions  as use_functions


def user_action():
   actions = int(input(f'''choose action:
1. создать папку;
2. удалить (файл/папку);
3. копировать (файл/папку);
4. просмотр содержимого рабочей директории;
5. посмотреть только папки;
6. посмотреть только файлы;
7.  создатель программы;
8. играть в викторину;
9. мой банковский счет;
10. смена рабочей директории (*необязательный пункт);
11. выход.'''))
   return actions


def create_folder(name_folder):
    """создать папку
    после выбора пользователь вводит название папки, создаем её в рабочей директории;"""
    os.mkdir(os.path.getcwd(), name_folder)

def drop_folder_or_file(item_to_drop):
    """удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
"""
    if os.path.exists(item_to_drop):
        if os.path.isfile(os.path.join(os.getcwd(), item_to_drop)):
            os.remove(os.path.join(os.getcwd(), item_to_drop))
        elif os.path.isdir(os.path.join(os.getcwd(), item_to_drop)):
            os.rmdir(os.path.join(os.getcwd(), item_to_drop))


def copy_file(item_to_copy):
    """после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;"""
    if os.path.isfile(os.path.join(os.getcwd(), item_to_copy)):
        os.copy(os.path.join(os.getcwd(), item_to_copy), os.path.join(os.getcwd(), item_to_copy))
    elif os.path.isdir(os.path.join(os.getcwd(), item_to_copy)):
        os.copy_tree(os.path.join(os.getcwd(), item_to_copy), os.path.join(os.getcwd(), item_to_copy))

def show_directory_content():
    """вывод всех объектов в рабочей папке;"""
    print(os.listdir(os.getcwd()))

def show_folders():
    """вывод только папок которые находятся в рабочей папке;"""
    for item in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), item)):
            print(item)
def show_files():
    """вывод только файлов которые находятся в рабочей папке;"""
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), item)):
            print(item)

def show_os_information():
    """вывести информацию об операционной системе (можно использовать пример из 1-го урока);"""
    print(platform.system())
    print(platform.release())
    print(platform.version())
    print(platform.machine())

def get_creator():
    """вывод информации о создателе программы;"""
    print('Creator Terekhova Mira')


def get_victorina():
    """запуск игры викторина из предыдущего дз;"""
    victory_game()

def get_bank_acc():
    """запуск программы для работы с банковским счетом из предыдущего дз"""
    use_functions()

def change_working_directory():
    new_path = input("Введите новый путь к директории: ")
    os.chdir(new_path)
    print(f"Текущая директория изменена на: {os.getcwd()}")



while user_action()!=13:
    action = user_action()

    if action == 1:
        name_folder = input('Введите название папки')
        create_folder(name_folder)

    elif action == 2:
        item_to_drop = input('Введите название файла или папки:')
        drop_folder_or_file(item_to_drop)

    elif action == 3:
        item_to_copy = input('Ввкдите название папки или файла для копирования')
        copy_file(item_to_copy)

    elif action == 4:
        show_directory_content()

    elif action== 5:
        show_folders()

    elif action == 6:
        show_files()

    elif action == 7:
        show_os_information()

    elif action == 8:
        get_creator()

    elif action == 9:
        get_victorina()

    elif action == 10:
        get_victorina()

    elif action == 11:
        get_bank_acc()

    elif action == 12:
        change_working_directory()

print("Выход из программы")









