import csv
import json

"""
Задание № 4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла
представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""


def csv_to_json(csv_file_name, json_file_name):
    try:
        with open(csv_file_name, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, dialect='excel',
                                    quoting=csv.QUOTE_ALL)
            header = next(csv_reader)

            data = []

            for row in csv_reader:
                user_name = row[0].capitalize()
                user_id = f'{int(row[1]):010}'
                user_hash = hash(f'{user_name}{user_id}')

                data.append({
                    'Имя': user_name,
                    'Личный идентификатор': user_id,
                    'Уровень доступа': row[2],
                    'Hash': user_hash
                })

        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    except FileNotFoundError:
        print(f'Файл не найден')


if __name__ == '__main__':
    csv_to_json('task_3.csv', 'task_4.json')
