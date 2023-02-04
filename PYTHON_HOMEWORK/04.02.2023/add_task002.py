"""
Напишите программу, которая найдет произведение пар чисел списка. Парой
считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import math
my_list = [2, 3, 4, 5, 6]


def multiply(lst):
    return [lst[i] * lst[-(i + 1)] for i in range(math.ceil(len(lst) / 2))]


print(multiply(my_list))

my_list = [2, 3, 5, 6]
print(multiply(my_list))

