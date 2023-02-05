"""
Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random

k = 2


def polynomial(number):
    string = str()
    for i in range(number, 0, -1):
        string += f'{random.randint(0, 100)} * x ** {i} + '
    string += f'{random.randint(0, 100)} = 0\n'
    return string


result = polynomial(k)
print(result)

with open('text004.txt', 'a', encoding='UTF-8') as file:
    file.write(result)
    file.close()
