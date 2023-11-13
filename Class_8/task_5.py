import os
import json
import pickle

"""
Задание № 5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их
содержимое в виде одноимённых pickle файлов.
"""

def json_to_pickle(directory):
    if not os.path.exists(directory):
        print(f'Директория не существует')
        return

    files = [file for file in os.listdir(directory) if file.endswith('.json')]

    for file_name in files:
        json_file_path = os.path.join(directory, file_name)
        pickle_file_path = os.path.join(directory, f'{os.path.splitext(file_name)[0]}.pickle')

        with (
            open(json_file_path, 'r', encoding='utf-8') as json_file,
            open(pickle_file_path, 'wb') as pickle_file
        ):
            data = json.load(json_file)
            pickle.dump(data, pickle_file)

if __name__ == '__main__':
    json_to_pickle('.')
