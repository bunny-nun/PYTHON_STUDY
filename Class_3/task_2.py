import re

"""
Пользователь вводит данные. Сделайте проверку данных и преобразуйте,
если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

user_input = input('Введите значение: ')
res = 0
# user_input = 1.01
if user_input.isdigit():
    res = int(user_input)
elif re.match(r'-?\d+\.\d+', user_input):
    res = float(user_input)
elif any(item.isupper() for item in user_input):
    res = user_input.upper()
else:
    res = user_input.lower()

print(res)

