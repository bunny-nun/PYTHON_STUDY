"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

data = [-5, 1, 2.1, True, -5, "Sds"]
# data = [True]

for item in data:
    try:
        if type(item) == str and not item.islower():
            print(item.lower())
        elif type(item) == str:
            print(item.lower())
        print(int(item))
        print(float(item))
    except ValueError:
        print('Невозможно преобразовать в целое или вещественное число')
        # print(item.lower())
    except TypeError:
        print('Ошибка')



