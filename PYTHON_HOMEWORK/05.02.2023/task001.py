"""
Вычислить число Пи c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
import time


def calculate_pi(d):

    start = time.time()
    pi = 4 * (1 - 1 / 3)
    counter = 0
    i = 2
    dif = 1
    while dif > float(d):
        my_list = list()
        my_list.append(4 * (-1) ** i / (2 * i + 1))
        i += 1
        my_list.append(4 * (-1) ** i / (2 * i + 1))
        i += 1
        dif = abs(my_list[0] - my_list[1])
        pi += my_list[0] + my_list[1]
        counter += 1
    pi_txt = str(pi)
    stop = time.time()
    print(pi_txt[:len(d)], counter, round(stop - start, 2))


calculate_pi('0.0000001')
