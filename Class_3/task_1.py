"""
✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый
список, который содержит уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие
коллекции помимо списков.
"""

original_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# 1
print(list(set(original_list)))

# new_set = set(original_list)
# new_list_1 = list(new_set)
# print(new_list_1)

# 2

new_list_2 = list()

for item in original_list:
    if item not in new_list_2:
        new_list_2.append(item)

print(new_list_2)