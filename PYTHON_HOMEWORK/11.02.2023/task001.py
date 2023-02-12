"""
Задание 1:
Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

start_operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')


def calculations(operation):
    operations = ['+', '-', '*', '/']

    if operation == '0':
        return
    else:
        if operation in operations:
            first_number = is_number(input('Введите первое число: '))
            second_number = zero_division(operation, is_number(
                input('Введите второе число: ')))

            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            else:
                result = first_number / second_number

            if result % 1 == 0:
                result = int(result)
            print(f'Ваш результат: {result}')
        return calculations(
            input('Введите операцию (+, -, *, / или 0 для выхода): '))


def is_number(number):
    if isinstance(number, float):
        return number
    try:
        number = float(number)
    except ValueError:
        number = input('Вы ввели некорректное значение. Введите число: ')
    return is_number(number)


def zero_division(test_operation, num):
    if not (test_operation == '/' and num == 0):
        return num
    return zero_division(test_operation, is_number(
        input('На ноль делить нельзя. Введите иное число: ')))


calculations(start_operation)
