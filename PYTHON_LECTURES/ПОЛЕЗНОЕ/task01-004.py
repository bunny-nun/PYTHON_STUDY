"""
Задача 4:
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""

together = int(input('Количество журавликов равно: '))

katya = int(together * 2 / 3)
petya_serezha = int(together / 6)

print(f'Петя: {petya_serezha}, Катя: {katya}, Сережа: {petya_serezha}')
