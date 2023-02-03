"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения
через list и через dict.
"""

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

# 1
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

if 3 <= month < 6:
    print(seasons[1])
elif 6 <= month < 9:
    print(seasons[2])
elif 9 <= month < 12:
    print(seasons[3])
else:
    print(seasons[0])

# 2
seasons_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8),
                'Осень': (9, 10, 11)}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)
