"""
Задание 26:
Напишите программу, которая на вход принимает два числа A и B, и возводит
число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""


def power(num, pow_num):
    if pow_num == 0:
        return 1
    elif pow_num == 1:
        return num
    else:
        return num * power(num, pow_num - 1)


number = int(input('Введите число: '))
power_number = int(input('Введите степень: '))
print(power(number, power_number))
