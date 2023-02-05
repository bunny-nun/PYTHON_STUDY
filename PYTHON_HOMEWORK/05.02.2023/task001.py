"""
Вычислить число Пи c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""


def calculate_pi(d):

    pi = 3
    counter = 0
    i = 2
    dif = 1
    while dif > float(d):
        my_list = list()
        my_list.append(4 / (i * (i + 1) * (i + 2)))
        my_list.append(4 / ((i + 2) * (i + 3) * (i + 4)))
        dif = abs(my_list[0] - my_list[1])
        pi += my_list[0] - my_list[1]
        counter += 1
        i += 4
        print(counter, pi)
    pi_txt = str(pi)
    print(d, len(d))
    print(pi_txt[:len(d)])


calculate_pi('0.000001')
