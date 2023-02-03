"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

n = int(input('Введите целое число: '))

# решение Дмитрия:
result, result_list = 1, {}
for i in range(1, n + 1):
    result += round((1 + 1 / n) ** n)
    result_list[i] = result
print(result_list)

# мое решение:
result_list = {}
for i in range(1, n + 1):
    result_list[i] = round(((1 + 1 / i) ** i), 2)
print(result_list)
