"""
Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности
"""

numbers = [1, 6, 7, 1, 8, 9, 0, 8]


def unique(lst):
    new_list = list()
    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique(numbers))
