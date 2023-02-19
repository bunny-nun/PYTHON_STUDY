"""
Задание 1:
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import os
import re


def get_data(directory):
    main_data = [['#', 'Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы']]
    prod_list, name_list, code_list, types_list = list(), list(), list(), list()
    for filename in os.listdir(directory):
        if filename.endswith('.txt') and filename != 'main_data.txt':
            with open(f'{filename}', 'r', encoding='UTF-8') as file:
                result = file.read()
                prod = re.compile(r'Изготовитель системы:\s*\S*')
                prod_list.append(prod.findall(result)[0].split()[2])
                name = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*\s*\S*')
                name = name.findall(result)[0]
                while '  ' in name:
                    name = name.replace('  ', ' ')
                name_list.append(name.split(': ')[1])
                code = re.compile(r'Код продукта:\s*\S*')
                code_list.append(code.findall(result)[0].split()[2])
                types = re.compile(r'Тип системы:\s*\S*')
                types_list.append(types.findall(result)[0].split()[2])

    for i in range(len(prod_list)):
        main_data.append(list())
        main_data[i + 1].append(f'{i + 1}')
        main_data[i + 1].append(prod_list[i])
        main_data[i + 1].append(name_list[i])
        main_data[i + 1].append(code_list[i])
        main_data[i + 1].append(types_list[i])

    with open('main_data.txt', 'w', encoding='UTF-8') as final_file:
        for row in main_data:
            final_file.write(f"{', '.join(row)}\n")

    return main_data


print(get_data('.'))


def write_to_csv(file_link):

    directory = os.path.dirname(file_link)
    lst = get_data(directory)
    with open(file_link, 'w', encoding='UTF-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerows(lst)


write_to_csv('./data_report.csv')


def writing_result(file_link):

    directory = os.path.dirname(file_link)
    lst = get_data(directory)
    with open(file_link, 'w', encoding='UTF-8') as file:
        file_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,
                                 delimiter='|')
        file_writer.writerows(lst)


# writing_result('./data_report.csv')


def reading_result(file_link):
    with open(file_link, encoding='UTF-8') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            if row:
                print(row)


def dict_result(file_link):
    with open(file_link, encoding='UTF-8') as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            if row:
                print(row)


def dict_result_param(file_link):
    with open(file_link, encoding='UTF-8') as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            if row:
                print(row['Изготовитель системы'])


reading_result('./data_report.csv')
dict_result('./data_report.csv')
dict_result_param('./data_report.csv')
