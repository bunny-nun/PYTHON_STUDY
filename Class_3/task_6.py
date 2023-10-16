"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

text = ("Apuleius Florida. Gaius Iulius Caesar De Bello Gallico. Cicero Pro "
        "Quincto. De Lege Agraria Contra Rullum!")

my_list = text.split()
my_list.sort()

space = max(len(item) for item in my_list)

for num, item in enumerate(my_list, 1):
    print(f'{num} {item:>{space}}')

print('***')

text = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()

shift = len(max(text))

for index, value in enumerate(sorted(text), 1):
    print(f'{index}. {value:>{shift}}')


