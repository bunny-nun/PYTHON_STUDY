"""
Создайте несколько объектов разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

lst = [1, True, 'string', 3.14, None, b'text']

for i in range(1, len(lst)):
    print(lst[i].__class__)

print()

for item in lst[1:]:
    print(type(item))
