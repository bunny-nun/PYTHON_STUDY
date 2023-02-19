"""
Задание 2:
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение
данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer),
дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с
передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

Вам нужно подгрузить JSON-объект и достучаться до списка, который и нужно
пополнять, а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as file:
        orders = json.load(file)

    orders['orders'].append(dict(
        {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer,
         'date': date}))
    with open('orders.json', 'w', encoding='UTF-8') as file:
        json.dump(orders, file, ensure_ascii=False, indent=4)


new_item = input('Введите наименование товара: ')
new_quantity = input('Введите количество товара: ')
new_price = input('Введите цену товара: ')
new_buyer = input('Введите имя покупателя: ')
new_date = input('Введите дату продажи товара: ')

write_order_to_json(new_item, new_quantity, new_price, new_buyer, new_date)

with open('orders.json', 'r', encoding='UTF-8') as new_file:
    result = json.load(new_file)
    for element in result['orders']:
        print(*element.values())
