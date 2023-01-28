"""
Задание 2.
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

seconds = int(input('Введите количество секунд: '))
minutes = round(seconds / 60, 3)
hours = round(minutes / 60, 3)
print(f'ч : м : с - {hours} : {minutes} : {seconds}')

# Перевод секунд в часы, минуты и секунды в формате "чч:мм:сс"

hours = int(seconds / 3600)
minutes = int(seconds / 60 - hours * 60)
new_seconds = seconds - minutes * 60 - hours * 3600

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if new_seconds < 10:
    new_seconds = '0' + str(new_seconds)

print(f'чч:мм:сс - {seconds} = {hours}:{minutes}:{new_seconds}')
