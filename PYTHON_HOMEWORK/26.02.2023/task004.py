"""
Задание 4:
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for i in my_list:
    i = i.encode(encoding='UTF-8')
    print(i, type(i))
    i = i.decode(encoding='UTF-8')
    print(i, type(i))
