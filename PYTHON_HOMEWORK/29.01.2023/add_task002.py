'''
Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.

Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

number = int(input('Введите целое число: '))
new_list = []

for i in range(1, number + 1):
    element = 1
    for j in range(2, i + 1):
        element *= j
    new_list.append(element)

print(new_list)
