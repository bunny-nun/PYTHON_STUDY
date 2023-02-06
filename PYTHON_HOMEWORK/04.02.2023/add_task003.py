"""
Задайте список из вещественных чисел. Напишите программу, которая найдет
разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random

my_list = [round(random.uniform(0, 100), 2) for i in range(10)]
print(my_list)
elements = [round(i - int(i), 2) for i in my_list]
print(elements)

result = round(max(elements) - min(elements), 2)
print(result)
