from random import randint, uniform

"""
Задание № 1
✔ Напишите функцию, которая заполняет файл (добавляет в конец) 
случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. 
"""

MIN_NUM = -1000
MAX_NUM = 1000


def num_pairs(raws, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(raws):
            print(
                f'{randint(MIN_NUM, MAX_NUM + 1)} | {uniform(MIN_NUM, MAX_NUM + 1)}',
                file=file)


if __name__ == '__main__':
    num_pairs(4, 'task_1.txt')
