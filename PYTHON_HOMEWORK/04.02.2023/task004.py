"""
Задание 4:
Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def get_list():
    txt_list = list()
    my_list = list()
    file = open('items.txt', 'r', encoding='UTF-8')
    count = 0
    for i in file.readlines():
        txt_list.append(i.split('\n')[0])
        item = txt_list[count].split(';')
        my_dict = {'Наименование': item[0], 'Цена': item[1],
                   'Количество': item[2], 'Ед.': item[3]}
        my_tuple = (count + 1, my_dict)
        my_list.append(my_tuple)
        count += 1
    file.close()
    return my_list


def add_item():
    to_add = int(input('Вы хотите добавить новый товар? '))
    if to_add:
        name = input('Введите название товара: ')
        price = int(input('Введите цену товара: '))
        amount = int(input('Введите количество товара: '))
        counter = input('Введите единицу изменения товара: ')
        new_record = f'{name};{price};{amount};{counter}\n'

        with open('items.txt', 'a', encoding='UTF-8') as file:
            file.write(new_record)
        file.close()
    print(get_list())


add_item()


def analytics():
    names, prices, amounts, counters = set(), set(), set(), set()
    my_list = get_list()
    for i in my_list:
        names.add(i[1]['Наименование'])
        prices.add(int(i[1]['Цена']))
        amounts.add(int(i[1]['Количество']))
        counters.add(i[1]['Ед.'])
    dictionary = {'Наименования': list(names), 'Цены': list(prices),
                  'Количества': list(amounts), 'Ед.': list(counters)}
    return dictionary


print(analytics())
