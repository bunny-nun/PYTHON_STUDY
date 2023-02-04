"""
Задание 1:
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""


month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

# 1
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']


def list_seasons(number, lst):
    if 3 <= number < 6:
        print(lst[1])
    elif 6 <= number < 9:
        print(lst[2])
    elif 9 <= number < 12:
        print(lst[3])
    else:
        print(lst[0])


list_seasons(month, seasons_list)

# 2
seasons_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8),
                'Осень': (9, 10, 11)}


def dict_seasons(number, dictionary):
    print(*[el for el in dictionary.keys() if number in dictionary.get(el)])


dict_seasons(month, seasons_dict)
