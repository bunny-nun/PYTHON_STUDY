"""
Задание 1.
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
Пример:
Введите Ваше имя: Василий
Введите Ваш пароль: vas
Введите Ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

name = 'Валерия'
age = 29
print(f'Имя: {name}, возраст: {age}')

name = input('Введите Ваше имя: ')
password = input('Введите Ваш пароль: ')
age = input('Введите Ваш возраст: ')

print(
    f'Ваши данные для входа в аккаунт: '
    f'имя - {name}, пароль - {password}, возраст - {age}')