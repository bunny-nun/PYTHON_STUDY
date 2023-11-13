import os.path
from os import urandom, makedirs, path, listdir
from random import choice, choices, randint
from string import ascii_lowercase

"""
Задание № 6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

def create_files(ext, dir, min_len=6, max_len=30, min_size=256, max_size=4096,
                 count=42):
    if not ext.startswith('.'):
        extension = '.' + ext

    if not path.exists(dir):
        makedirs(dir)

    for _ in range(count):
        name = ''.join(
            choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        while name in listdir(dir):
            name + choice(ascii_lowercase)
        name = os.path.join(dir, name)
        size = randint(min_size, max_size)

        with open(name, 'wb') as file:
            data = urandom(size)
            file.write(data)


if __name__ == '__main__':
    create_files('.txt', '..', min_len=4, max_len=6, min_size=512, max_size=2048,
                 count=1)
