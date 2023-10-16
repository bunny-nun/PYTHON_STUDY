"""
На вход подается словарь со списком вещей для похода в качестве ключа и их
массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную
грузоподъёмность.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и
сохранен в переменную backpack.

Достаточно вернуть один допустимый вариант.
"""
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
#
# backpack = {}
#
# backpack_weight = 0
#
# for key in items:
#     if backpack_weight + items[key] <= max_weight:
#         backpack[key] = items[key]
#         backpack_weight += items[key]
# print(backpack)

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
#
backpack = {}
# backpack_weight = 0
#
# for key, weight in items.items():
#     if weight <= max_weight - backpack_weight:
#         backpack[key] = weight
#         backpack_weight += weight
# print(backpack)

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
        print(max_weight)

print(backpack)