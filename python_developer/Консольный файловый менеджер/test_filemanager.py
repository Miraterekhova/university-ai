import sys
import os
from unittest.mock import patch
import pytest
import shutil




sys.path.append(os.path.join(os.getcwd(), 'Консольный файловый менеджер'))

from main import (
    create_folder,
    drop_folder_or_file,
    copy_file,
    show_directory_content,
    show_folders,
    show_files,
    show_os_information,
    get_creator,
    change_working_directory
)

TEST_DIRECTORY = os.path.join(os.getcwd(), 'test_directory')


@pytest.fixture(autouse=True)
def setup_and_teardown():
    TEST_DIRECTORY = 'test_directory'

    # Создание временной папки перед тестами
    if not os.path.exists(TEST_DIRECTORY):
        os.makedirs(TEST_DIRECTORY)
    os.chdir(TEST_DIRECTORY)

    yield  # Выполнение тестов

    # Удаление временной папки после тестов
    os.chdir('..')  # Вернуться в родительскую директорию
    if os.path.exists(TEST_DIRECTORY):
        shutil.rmtree(TEST_DIRECTORY)  # Удаляем директорию рекурсивно


def test_create_folder():
    folder_name = 'test_folder'
    create_folder(folder_name)

    assert os.path.exists(folder_name) and os.path.isdir(folder_name)


def test_drop_folder():
    folder_name = 'folder_to_delete'
    os.makedirs(folder_name)

    drop_folder_or_file(folder_name)
    assert not os.path.exists(folder_name)


def test_drop_file():
    file_name = 'file_to_delete.txt'
    with open(file_name, 'w') as f:
        f.write('Hello World')

    drop_folder_or_file(file_name)
    assert not os.path.exists(file_name)


def test_copy_file():
    file_name = 'test_file.txt'
    with open(file_name, 'w') as f:
        f.write('Hello World')

    copy_file(file_name)
    assert os.path.exists(f'copy_{file_name}')  # Проверить, что файл был скопирован


def test_show_directory_content(mocker):
    mock_print = mocker.patch('builtins.print')
    file_name = 'file_to_show.txt'
    with open(file_name, 'w') as f:
        f.write('Hello World')

    show_directory_content()
    mock_print.assert_any_call(file_name)


def test_show_folders(mocker):
    mock_print = mocker.patch('builtins.print')
    folder_name = 'folder_to_show'
    os.makedirs(folder_name)

    show_folders()
    mock_print.assert_any_call(folder_name)


def test_show_files(mocker):
    mock_print = mocker.patch('builtins.print')
    file_name = 'file_to_show.txt'
    with open(file_name, 'w') as f:
        f.write('Hello World')

    show_files()
    mock_print.assert_any_call(file_name)


def test_get_creator(mocker):
    mock_print = mocker.patch('builtins.print')
    get_creator()
    mock_print.assert_any_call('Creator Terekhova Mira')


def test_change_working_directory():
    new_directory = 'new_folder'

    # Создаем новую папку для теста
    os.mkdir(new_directory)

    with patch('os.chdir') as mock_chdir, patch('builtins.input', return_value=new_directory):
        # Вызов функции для изменения рабочего каталога
        change_working_directory()

        # Проверяем, что os.chdir была вызвана с правильным аргументом
        mock_chdir.assert_called_once_with(new_directory)

    # Удаление тестовой директории после теста
    os.rmdir(new_directory)


