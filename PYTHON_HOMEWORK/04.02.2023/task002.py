"""
Задание 2:
Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

new_list = input('Введите слова через пробел: ').split()


def split_string(lst):
    for i in range(len(lst)):
        print(f'{i + 1}. {lst[i][:10]}')


split_string(new_list)
