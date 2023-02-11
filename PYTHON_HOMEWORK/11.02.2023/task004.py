"""
Задание 4:
Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""

num = int(input('Введите количество элементов: '))


def count_array(number, element=float(1)):
    if number == 1:
        return element
    number -= 1
    return element + count_array(number, -(element / 2))


result = count_array(num)
if result % 1 == 0:
    print(int(result))
else:
    print(result)
