dictionary = {1: 'wow', 2: 'hello'}
print(dictionary[1])  # обращение по ключу, а не по индексу

a = dictionary.get(3)
print(a)

print(dictionary)

b = dictionary.pop(1)
print(b)
print(dictionary)

new_dictionary = {}
print(type(new_dictionary))  # <class 'dict'> НЕ МНОЖЕСТВО!

print('==============')

new_set = {'one', 'two', 'three'}
print(type(new_set))  # <class 'set'> МНОЖЕСТВО!

print('==============')

set_01 = {1, 2, 3, 4, 5}

set_02 = set_01.copy()
print(set_02)

set_02 = {5, 6, 7, 8, 9, 10}
print(set_02)

set_03 = set_01.union(set_02)  # объединение
print(set_03)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set_03 = set_01.intersection(set_02)  # пересечение
print(set_03)  # {5}

set_03 = set_01.difference(set_02)  # разница
print(set_03)  # {1, 2, 3, 4}

set_03 = set_02.difference(set_01)
print(set_03)  # {6, 7, 8, 9, 10}
