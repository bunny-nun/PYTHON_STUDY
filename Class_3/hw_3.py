"""
На вход подается словарь со списком вещей для похода в качестве ключа и их
массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную
грузоподъёмность.

В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.

В переменную result выведите список, содержащий все возможные варианты
backpack.

*Верните все возможные варианты комплектации рюкзака.
"""
items = {
    "a": 0.3,
    "b": 0.2,
    "c": 0.5,
    "d": 0.1
}

max_weight = 1.0

"""
[{'a': 0.3},
 {'b': 0.2},
 {'a': 0.3, 'b': 0.2},
 {'c': 0.5},
 {'a': 0.3, 'c': 0.5},
 {'b': 0.2, 'c': 0.5},
 {'a': 0.3, 'b': 0.2, 'c': 0.5},
 {'d': 0.1},
 {'d': 0.1, 'a': 0.3},
 {'d': 0.1, 'b': 0.2},
 {'d': 0.1, 'a': 0.3, 'b': 0.2},
 {'d': 0.1, 'c': 0.5},
 {'d': 0.1, 'a': 0.3, 'c': 0.5},
 {'d': 0.1, 'b': 0.2, 'c': 0.5},
 {'a': 0.3, 'b': 0.2, 'c': 0.5}]
"""

# Ваш словарь предметов и максимальный вес
items = {
    "ноутбук": 2.0,
    "книги": 1.5,
    "зарядное устройство": 0.5,
    "бутерброды": 0.3,
    "вода": 1.0
}
max_weight = 5.0

item_indices = list(range(len(items)))

result = []

for mask in range(1 << len(items)):
    current_combination = {}
    remaining_weight = max_weight

    for index in item_indices:
        if (mask >> index) & 1:
            item = list(items.keys())[index]
            weight = items[item]
            if weight <= remaining_weight:
                current_combination[item] = weight
                remaining_weight -= weight

    if remaining_weight >= 0:
        if len(current_combination) > 0:
            sorted_dict = dict(sorted(current_combination.items()))
            result.append(sorted_dict)

print(f'[{result[0]},')
for i in range(1, len(result) - 1):
    print(f'{result[i]},')
print(f'{result[-1]}]')




#
#     max_weight = 1.0
#     backpack = {}
#     key = keys[i]
#     weight = items[key]
#     if weight <= max_weight:
#         backpack[key] = weight
#         result.append(backpack.copy())
#         max_weight -= weight
#         if i - 1 > 0:
#         for j in range(i):
#             max_weight = 1.0
#             backpack = {}
#             if w <= max_weight:
#                 backpack[i] = w
#                 result.append(backpack.copy())
#                 max_weight -= w
#             if i == item:
#                 break
#
# print(result)

from pprint import pprint

backpacks = []

for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

result = [backpack for backpack in backpacks if backpack]

pprint(result)
