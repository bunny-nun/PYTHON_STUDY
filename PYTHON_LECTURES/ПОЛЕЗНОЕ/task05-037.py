"""
Задание 37:
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""


def generate_numbers(num, counter=1):
    if counter == num:
        return str(num + counter)
    return f'{num + counter} {generate_numbers(num, counter + 1)}'


def reverse_numbers(result):
    if len(result.split(' ')) == 1:
        return result
    else:
        result = result.split(' ')
    return str(result[-1]) + ' ' + reverse_numbers(
        ' '.join(result[:len(result) - 1]))


number = int(input('Введите натуральное число: '))
print(generate_numbers(number))
print(reverse_numbers(generate_numbers(number)))
