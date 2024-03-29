"""
Задание 3:
Задание на закрепление знаний по модулю yaml.  Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml
from yaml.loader import SafeLoader

with open('file.yaml', 'r', encoding='UTF-8') as file:
    file_content = yaml.load(file, SafeLoader)

print(file_content)

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_quantity': 4,
        'items_price': {'computer': '200\u20AC-1000\u20AC',
                        'keyboard': '5\u20AC-50\u20AC',
                        'mouse': '4\u20AC-7\u20AC',
                        'printer': '100\u20AC-300\u20AC'}}

print(data)

with open('file.yaml', 'w', encoding='UTF-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True,
              sort_keys=False)
