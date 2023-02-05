"""
Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N
"""


def factors(numbers):
    index = 2
    factors_list = list()
    while index ** 2 <= numbers:
        while numbers % index == 0:
            factors_list.append(index)
            numbers /= index
        index += 1
    if numbers > 1:
        factors_list.append(int(numbers))
    return set(factors_list)


print(*factors(3628800))
