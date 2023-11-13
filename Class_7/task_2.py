from random import randint, choice
from math import floor
"""
Задание № 2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

def generate_name():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name_len = randint(4, 7)

    name = [choice(vowels + consonants).upper()]

    for i in range(name_len - 1):
        name.append(choice(consonants))
    for i in range((name_len - 1) // 2):
        name[choice(range(1, name_len - 1))] = choice(vowels)
    return ''.join(name)

def save_names(count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(count):
            print(generate_name(), file=file)


if __name__ == '__main__':
    save_names(5, 'task_2.txt')
