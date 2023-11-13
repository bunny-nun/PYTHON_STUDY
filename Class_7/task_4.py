from os import urandom
from random import choices, randint
from string import ascii_lowercase

"""
Задание № 4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

"""


def create_files(ext, min_len=6, max_len=30, min_size=256, max_size=4096,
                 count=42):
    if not ext.startswith('.'):
        extension = '.' + ext

    for _ in range(count):
        name = ''.join(
            choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_size, max_size)

        with open(name, 'wb') as file:
            data = urandom(size)
            file.write(data)


if __name__ == '__main__':
    create_files('.txt', min_len=4, max_len=6, min_size=512, max_size=2048,
                 count=2)
