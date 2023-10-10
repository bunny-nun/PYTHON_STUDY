import decimal
import math

"""
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.

"""

try:
    d = int(input('число: '))
except ValueError:
    print('Ошибка')
else:
    decimal.getcontext().prec = 42
    s = math.pi * (d / 2) ** 2
    print(s)

    c = math.pi * d
    print(c)

    # print(f'{s:.2f}')
finally:
    print('***')