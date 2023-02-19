"""
Задание 5:

Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном
примере. Необходимо запрашивать у пользователя данные и заполнять список только
числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду
“stop”. При этом скрипт завершается, сформированный список с числами выводится
на экран.
Подсказка: для данного задания примем, что пользователь может вводить только
числа и строки. При вводе пользователем очередного элемента необходимо
реализовать проверку типа элемента и вносить его в список, только если введено
число. Класс-исключение должен не позволить пользователю ввести текст
(не число) и отобразить соответствующее сообщение. При этом работа скрипта
не должна завершаться.
"""


class NotNumber(Exception):
    def __init__(self, text):
        self.text = text


def number_list(num, lst=None):
    if lst is None:
        lst = []
    if num == 'stop':
        print(lst)
        return
    lst.append(is_number(num))
    return number_list(input('Введите число (stop для выхода): '), lst)


def is_number(number):
    if isinstance(number, str):
        raise NotNumber('Вы ввели некорректное значение. Введите число: ')
    try:
        number = int(number)
        return number
    except NotNumber as error:
        return is_number(input(error))


number_01 = input('Введите число: ')
number_list(number_01)
