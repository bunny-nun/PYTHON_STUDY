"""
Задание 6:
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

number = random.randint(0, 100)
guess = int(input('Попыток осталось: 10. Введите число: '))


def guess_number(num, new_guess, attempts=9):
    if new_guess == num:
        print(f'Вы угадали! Число равно {num}')
        return
    elif attempts == 0:
        print(f'Вы не угадали! Число равно {num}')
        return
    else:
        if num < new_guess:
            print('Загаданное число меньше')
        if num > new_guess:
            print('Загаданное число больше')
        return guess_number(num, int(input(
            f'Попыток осталось: {attempts}. Введите число: ')), attempts - 1)


guess_number(number, guess)
