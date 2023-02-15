"""
Задание 31:
Последовательностью Фибоначчи называется последовательность чисел
a0, a1, ..., an, ..., где a0  = 0, a1  = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13

"""


def fibonacci(index):
    if index < 2:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


n = int(input('Введите число: '))
print(fibonacci(n))
