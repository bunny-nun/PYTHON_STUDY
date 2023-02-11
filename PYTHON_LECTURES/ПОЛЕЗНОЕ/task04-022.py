"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

"""
import random

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

list_n = [random.randint(0, 9) for i in range(n)]
list_m = [random.randint(0, 9) for i in range(m)]

print(list_n, list_m)


def repeated_elements(list_01, list_02):
    return sorted(set([number for number in list_01 if number in list_02]))


print(repeated_elements(list_n, list_m))
