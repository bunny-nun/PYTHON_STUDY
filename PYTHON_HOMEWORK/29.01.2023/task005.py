"""
Задание 5.
Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки. Строки необходимо
пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

new_list = input('Введите слова через пробел: ')
new_list = new_list.split()

for i in range(len(new_list)):
    print(f'{i + 1}. {new_list[i][:10]}')

