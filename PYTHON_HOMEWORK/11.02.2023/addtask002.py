"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у
своего конкурента?
1) Добавьте игру против бота
2) Подумайте как наделить бота "интеллектом"
"""
import random


def is_number(number):
    if isinstance(number, int):
        return number
    try:
        number = int(number)
    except ValueError:
        number = input('Введено неверное значение. Укажите: да - 1, нет - 0: ')
    return is_number(number)


def start_game():
    player_01 = input('Введите имя первого игрока: ')
    comp = is_number(input(
        'Вы хотите играть с компьютером? да - 1, нет - 0: '))
    while comp != (0 or 1):
        comp = is_number(input(
            'Введено неверное значение. Укажите: да - 1, нет - 0: '))
    if comp:
        player_02 = 'Компьютер'
    else:
        player_02 = input('Введите имя второго игрока: ')
    start_value = int(input('Введите количество конфет на столе: '))
    game_limit = int(input('Введите максимальное количество конфет за ход: '))

    start_game_flag = random.randint(0, 2)  # флаг очередности
    if start_game_flag:
        print(f'Первым ходит {player_01}')
    else:
        print(f'Первым ходит {player_02}')
    return player_01, player_02, comp, start_value, game_limit, start_game_flag


def first_turn(start_value, turn_max, flag, player_01_name):
    if flag:
        turn_01 = new_turn(player_01_name, turn_max)
        flag, who_first = False, False
    else:
        if start_value % turn_max == 0:
            turn_01 = turn_max - 1
        else:
            turn_01 = start_value % turn_max - 1
        flag, who_first = True, True
        print(f'Ходит Компьютер. Взято количество конфет: {turn_01}')
    print_turn_result(start_value - turn_01)
    return start_value - turn_01, flag, who_first, turn_01


def new_turn(name, limit):
    turn = int(input(f'Ходит {name}. Введите количество конфет: '))
    while 1 > turn > limit:
        turn = int(input(
            f'Введите корректное количество конфет (не более {limit}): '))
    return turn


def print_turn_result(value_left):
    print(f'На столе осталось {value_left} конфет.')


def game(value, flag, limit, player_1_name, player_2_name):
    if value == 0:
        return flag
    else:
        if flag:
            player = player_1_name
        else:
            player = player_2_name
        turn_amount = new_turn(player, limit)
        value -= turn_amount
        if flag:
            flag = False
        else:
            flag = True
        print_turn_result(value)
        return game(value, flag, limit, player_1_name,
                    player_2_name)


def computer_game(comp_first, prev_turn, value, flag, limit, player_1_name):
    if value == 0:
        return flag
    else:
        if flag:
            turn_amount = new_turn(player_1_name, limit)
            prev_turn = turn_amount
            flag = False
        else:
            if value <= limit:
                turn_amount = value
            else:
                if comp_first:
                    turn_amount = limit - prev_turn
                    if turn_amount == 0:
                        turn_amount = limit
                else:
                    turn_amount = random.randint(1, limit)
            print(f'Ходит Компьютер. Взято количество конфет: {turn_amount}')
            flag = True
        value -= turn_amount
        print_turn_result(value)
        return computer_game(comp_first, prev_turn, value, flag, limit,
                             player_1_name)


player_1, player_2, computer, total_value, turn_limit, start_flag = start_game()

if computer:
    total_value, start_flag, computer_first, previous_turn = first_turn(
        total_value, turn_limit, start_flag, player_1)
    result = computer_game(computer_first, previous_turn, total_value,
                           start_flag, turn_limit, player_1)
else:
    result = game(total_value, start_flag, turn_limit, player_1, player_2)

if result:
    print(f'Выиграл(-а) {player_2}')
else:
    print(f'Выиграл(-а) {player_1}')
