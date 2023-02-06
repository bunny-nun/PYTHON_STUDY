"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
индексов.

Пример:

- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

number = int(input('Введите число: '))
fibonacci = [0, 1]
for i in range(2, number + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

for j in range(1, len(fibonacci) * 2 - 1, 2):
    fibonacci.insert(0, -(fibonacci[j]))

print(fibonacci)
