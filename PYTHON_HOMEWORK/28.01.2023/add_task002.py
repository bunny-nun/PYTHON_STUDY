"""
Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
"""
x = 0
y = 0
z = 0

statement_left = not (x or y or z)
statement_right = (not x) and (not y) and (not z)

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'x = {x}, y = {y}, z = {z}, statement = '
                  f'{statement_left == statement_right}')
