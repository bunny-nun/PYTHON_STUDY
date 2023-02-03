"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.
"""

import random

length = int(input('Введите число: '))
numbers = list(range(-length, length + 1))
print(f'numbers: {numbers}')

file = open('positions.txt', 'r', encoding='UTF-8')
positions = []
for i in file.readlines():
    positions.append(int(i))
file.close()
print(f'positions: {positions}')

result = 1
for i in positions:
    result *= numbers[i]

print(f'result: {result}')

print("random numbers: ", end="")

print(random.sample(numbers, len(numbers)))


