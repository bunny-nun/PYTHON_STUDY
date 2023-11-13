import json

"""
Задание № 2
Напишите функцию, которая в бесконечном цикле запрашивает имя, 
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. 
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

def add_user():
    try:
        with open('task_2.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.decoder.JSONDecodeError:
        data = {}

    while True:
        print(data)
        user_name = input('Введите имя пользователя или "0" для выхода: ')
        if user_name == '0':
            break

        user_id_is_unique = False
        while not user_id_is_unique:
            user_id = input('Введите личный идентификатор: ')
            user_id_is_unique = all(user_id not in level.keys() for level in data.values())
            if not user_id_is_unique:
                print('Идентификатор занят, введите другой')

        user_level = input('Введите уровень доступа (от 1 до 7): ')
        while not user_level.isdigit() or not (1 <= int(user_level) <= 7):
            print('Уровень доступа должен быть целым числом от 1 до 7')
            user_level = input('Введите уровень доступа (от 1 до 7): ')

        if user_level not in data:
            data[user_level] = {}

        data[user_level][user_id] = user_name

        with open('task_2.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2, sort_keys=True)

        print(f'Пользователь {user_name} успешно добавлен с идентификатором {user_id} и уровнем доступа {user_level}')

if __name__ == '__main__':
    add_user()
