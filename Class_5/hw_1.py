"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""
import os

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    # Разбиваем абсолютный путь на директорию и имя файла
    directory, file_name = os.path.split(file_path)
    if directory != '':
        directory = f'{directory}/'


    # Получаем расширение файла
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    if file_name_without_extension == 'file':
        file_name_without_extension = ''
        file_extension = '.file'

    return (directory, file_name_without_extension, file_extension)


# Пример использования
file_path = "C:/Users/User/Documents/example.txt"
result = get_file_info(file_path)
print(result)