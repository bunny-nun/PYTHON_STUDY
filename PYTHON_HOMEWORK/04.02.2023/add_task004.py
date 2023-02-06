"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

number = float(input('Введите число: '))


def to_binary(num):
    fraction = num - int(num)
    num = int(num)
    binary_num, binary_frac = list(), list()
    while num > 0:
        binary_num.append(num % 2)
        num //= 2
    result = str()
    for i in range(-1, -len(binary_num) - 1, -1):
        result += str(binary_num[i])
    if fraction > 0:
        result += '.'
        while fraction < 1:
            fraction *= 2
            binary_frac.append(int(fraction))
        for i in range(len(binary_frac)):
            result += str(binary_frac[i])

    return(result)


print(f'{number} = {to_binary(number)}')
print(f'check: {bin(int(number))}')
