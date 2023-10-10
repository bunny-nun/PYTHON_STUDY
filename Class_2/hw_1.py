"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


num = 0
hex_characters = '0123456789ABCDEF'
result = ''

if num > 0:
    number = num
    while number > 0:
        remainder = number % 16
        result = hex_characters[remainder] + result
        number //= 16
elif num < 0:
    number = num * -1
    while number > 0:
        remainder = number % 16
        result = hex_characters[remainder] + result
        number //= 16
    result = '-' + result

print(f'Шестнадцатеричное представление числа: {result}')
print(f'Проверка результата: {hex(num)}')
