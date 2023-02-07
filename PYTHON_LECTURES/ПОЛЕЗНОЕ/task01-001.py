"""
Найдите сумму цифр трехзначного числа
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

"""

number = input('Введите трехзначное число: ')
result = sum([int(i) for i in number])
print(result)
