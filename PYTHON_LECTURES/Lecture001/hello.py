a = 123
b = 1.23
print(type(a))  # Вывести тип переменной
print(type(b))

value = None  # Объявление пустой переменной
print(type(value))
value = 1234
print(type(value))

print('=========')

s = "hello 'world'"  # Можно использовать разные кавычки, чтобы одни из них распечатались внутри текста

print(s)  # Вывод строки

s = 'hello \' world'  # Слэш перед кавычкой, чтобы указать ее как символ внутри кавычек
print(s)

s = 'hello world'
print(s)

print(s.capitalize())

print(s.upper())

print('=========')

print(a, '-', b, '-', s)

print('{} - {} - {}'.format(a, b, s))

print(f'{a} - {b} - {s}')

print('{1} - {0} - {2}'.format(b, a, s))  # Изменить порядок вывода по индексу

f = True
print(f)
print(type(f))

newList = []  # Задание пустого массива
newList = [1, 2, 3]
print(newList)

newList = ['a', 'b', 'c', 1, 1.23]  # Массив может содержать разные типы данных
print(newList)
print(type(newList))

# print('Введите число a: ')
# a = int(input())
# print('Введите число b: ')
# b = int(input())
# print('a = ', a, 'b =', b, 'a + b =', a + b)

# print('Введите число a: ')
# a = float(input())
# print('Введите число b: ')
# b = float(input())
# print('a = ', a, 'b =', b, 'a + b =', a + b)

a = 12
b = 8
c = a / b
print(c)

c = a // b
print(c)

a = 1.3
b = 3
c = round(a * b, 3)
print(c)

c = 3.1234567
c = round(c, 4)
print(c)

a = 1 > 3
print(a)

a = 1 < 3 and 5 > 4
print(a)

a = 1 < 3 or 3 > 4
print(a)

a = 1 == 4
print(a)

a = 1 != 4
print(a)

a = 1 < 3 < 5
print(a)

# func = 1
# T = 4
# x = 2
# print(func < T > x)

print('=========')

f = [1, 2, 3, 4]
print(f)
print(2 in f)
print(5 in f)
print(not 5 in f)

print('=========')

is_odd = f[1] % 2 == 0
print(is_odd)

is_odd = not f[1] % 2
print(is_odd)

print('=========')

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
# print(a)
# else:
# print(b)

# print('=========')

# original = int(input('Введите число: '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('The end')
# print(inverted)

# print('=========')

for i in range(1, 10):
    print(i ** 2)

num = 1.67
print(type(num), num)

# num = input()
# print(type(num), num)
# num *= 3
# print(type(num), num)

num = int(num)
print(type(num), num)
num = str(num)
print(type(num), num)
