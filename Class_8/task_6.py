import pickle
import csv

"""
Задание № 6
Напишите функцию, которая преобразует pickle файл хранящий список словарей
в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""

import pickle
import csv


def pickle_to_csv(pickle_file_name, csv_file_name):
    try:
        with (
            open(pickle_file_name, 'rb') as pickle_file,
            open(csv_file_name, 'w', encoding='utf-8', newline='') as csv_file
        ):
            data = pickle.load(pickle_file)
            header = data[0].keys()

            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)


    except FileNotFoundError:
        print(f'Файл не найден')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    pickle_to_csv('task_4.pickle', 'task_6.csv')
