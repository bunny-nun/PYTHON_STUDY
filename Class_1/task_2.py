"""
Задание №5
📌 Работа в консоли в режиме интерпретатора Python.
📌 Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
📌 Используйте while и if.
📌 Попробуйте разные значения e и n.
"""

n = 20
e = 3

sum_value = 0

element = 1

while element <= n:
    if element % 2 == 0 and element % e != 0:
        sum_value += element
    element += 1

print(sum_value)
