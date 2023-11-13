import json
import csv

"""
Задание № 3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""


def json_to_csv():
    with (
        open('task_2.json', 'r', encoding='utf-8') as users_json,
        open('task_3.csv', 'w', encoding='utf-8', newline='') as users_csv
    ):
        data = json.load(users_json)
        csv_writer = csv.writer(users_csv)
        csv_writer.writerow(['Имя', 'Личный идентификатор', 'Уровень доступа'])

        for user_level, users in data.items():
            for user_id, user_name in users.items():
                csv_writer.writerow([user_name, user_id, user_level])

if __name__ == '__main__':
    json_to_csv()
