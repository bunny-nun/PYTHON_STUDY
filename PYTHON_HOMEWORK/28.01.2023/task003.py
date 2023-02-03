"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел = n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

number = input('Введите целое положительное число n: ')
sum_value = int(number) + int(number * 2) + int(number * 3)
print(f'n + nn + nnn = {sum_value}')
