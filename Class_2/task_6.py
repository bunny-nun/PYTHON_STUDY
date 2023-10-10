"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

num = 0
count = 0
per_cent = 0


while 1:
    action = input('Выберите тип действия: ')
    if action == 'q':
        print('Выход из банкомата')
        print(num)
        break
    elif action == 'a':
        num_add = int(input('Введите сумму пополнения: '))
        if num_add % 50 == 0:
            num += num_add
            count += 1
            if count % 3 == 0:
                per_cent = num * 0.03
                num -= per_cent
        else:
            print('Некорректная сумма')
        print(num)
    elif action == 'o':
        num_out = int(input('Введите сумму снятия: '))
        if num_out % 50 == 0:
            if count % 3 == 0:
                per_cent = num * 0.03
            else:
                per_cent = num * 0.015
            if per_cent < 30:
                per_cent = 30
            elif per_cent > 600:
                per_cent = 600
            if (num_out + per_cent) < num:
                num -= num_out + per_cent
                count += 1
            else:
                print('Недостаточно денег на счете')
        else:
            print('Некорректная сумма')
        print(num)
