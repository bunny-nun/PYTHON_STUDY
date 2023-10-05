"""
Задание №6
📌 Напишите программу, которая запрашивает год и проверяет его на високосность.
📌 Распишите все возможные проверки в цепочке elif
📌 Откажитесь от магических чисел
📌 Обязательно учтите год ввода Григорианского календаря
📌 В коде должны быть один input и один print
"""

year = 2016


def func_1(user_year):
    if user_year % 400 == 0 or (user_year % 4 == 0 and user_year % 100 != 0):
        res = f'Год {user_year} - високосный'
    else:
        res = f'Год {user_year} - невисокосный'
    return res


def func_2(user_year):
    return f'Год {user_year} - високосный' if user_year % 400 == 0 or (
                user_year % 4 == 0 and user_year % 100 != 0) else f'Год {user_year} - невисокосный'


print(func_1(year))
print(func_2(year))
