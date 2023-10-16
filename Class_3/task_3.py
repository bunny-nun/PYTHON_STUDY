"""
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

my_tuple = (1, 'text', None, True, 1.01, [1, 2])

my_dict = dict()

for item in my_tuple:
    obj_type = type(item)
    lst = []
    for el in my_tuple:
        if type(el) == obj_type:
            lst.append(el)

    my_dict[obj_type] = lst
print(my_dict)