"""
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.
"""

lst = [1, 2, 3, 2, 4, 5, 4]
res = []

for item in lst:
    if lst.count(item) > 1:
        res.append(item)


print([i for i in list(set(res))])