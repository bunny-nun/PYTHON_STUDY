import random

# заполнить список нечетными числами
new_list = [i for i in range(1, 101, 2)]
print(new_list)

# заполнить список числами, которые делятся на 3
new_list = [i for i in range(1, 101) if i % 3 == 0]
print(new_list)

# заполнить список случайными числами
new_list = [random.randint(0, 9) for i in range(20)]
print(new_list)

# заполнить список простыми числами
new_list = []
for i in range(1, 101):
    is_simple = True
    for j in range(2, i):
        if i % j == 0:
            is_simple = False
    if is_simple:
        new_list.append(i)
print(new_list)
