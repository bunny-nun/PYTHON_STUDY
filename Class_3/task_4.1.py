"""
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]

dct = {}

for item in lst:
    dct[item] = dct.get(item, 0) + 1

new_lst = [el for el in lst if dct[el] != 2]

print(*new_lst)