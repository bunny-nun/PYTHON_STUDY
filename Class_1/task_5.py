"""
Задание №8
📌 Нарисовать в консоли ёлку спросив у пользователя количество рядов.
📌 Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = 5
space = ' '
symbol = '*'

symbols = 1
spaces = rows - 1

for i in range(rows):
    print((space * spaces) + (symbol * symbols) + (space * spaces))
    symbols += 2
    spaces -= 1
