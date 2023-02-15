"""
Задание 35:
Напишите функцию, которая принимает одно число и проверяет, является ли оно
простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и
n (само число)
Input: 5
Output: yes
"""


def is_simple(number, index):
    if index == 1:
        return True
    else:
        if number % index == 0:
            return False
        return is_simple(number, index - 1)


num = int(input('Введите число: '))
print(is_simple(num, num - 1))
