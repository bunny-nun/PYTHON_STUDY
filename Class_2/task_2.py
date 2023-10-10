from sys import getsizeof

"""
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.

"""

data = [5, 5, 'Hello World', 'Hello World', True, None, 15.23]

for i in range(len(data)):
    print(f'порядковый номер: {i + 1}')
    print(f'значение: {data[i]}')
    print(f'тип объекта: {type(data[i])}')
    print(f'адрес в памяти: {id(data[i])}')
    print(f'размер в памяти: {getsizeof(data[i])}')
    if isinstance(data[i],
                  (int, str, bool, float, complex, tuple, bytes, frozenset)):
        print(f'хэш объекта: {hash(data[i])}')
    if str(data[i]).isdigit():
        print('является целым числом')
    if isinstance(data[i], str):
        print('является строкой')
    print()

    print('***')

for i, value in enumerate(data, 1):
    print(f'{i} . {value} . {id(value)} . {value.__sizeof__()} . {hash(value)}')
    if type(value) == int and value > 0:
        print('целое положительное число')
    elif type(value) == str:
        print('строка')
