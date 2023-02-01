my_string = input('Введите текст: ')


def add_length(str_):
    return [f'{i} {str(len(i))}' for i in str_.split()]


print(add_length(my_string))
