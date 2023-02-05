"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов
"""

result, ratios, polynomial = list(), list(), list()


def read_file(file_txt):
    with open(file_txt, 'r', encoding='UTF-8') as file:
        for i in file.readlines():
            result.append(i.split('\n')[0].split(' + '))
        file.close()


read_file('text004.txt')
read_file('text005.txt')

print(result)


def polynomial_read(collection):
    string = str()
    a = max([len(lst) for lst in collection])
    for obj in range(-1, -a - 1, -1):
        ratio = 0
        for j in range(len(collection)):
            if abs(obj) <= len(collection[j]):
                ratio += int(collection[j][obj][:2])
        ratios.append(ratio)
    for i in range(-1, -a, -1):
        string += f'{ratios[i]} * x ** {abs(i)} + '
    string += f'{ratios[0]} = 0\n'
    print(string)
    return string


with open('text005-1.txt', 'w', encoding='UTF-8') as file:
    file.write(polynomial_read(result))
    file.close()




