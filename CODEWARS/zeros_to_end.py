"""
Write an algorithm that takes an array and moves all the zeros to the end,
preserving the order of the other elements.
"""


def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(lst[i])
            del lst[i]
    return lst


def move_zeros_2(lst):
    new_list = [i for i in lst if i != 0]
    new_list.extend([i for i in lst if i == 0])
    return new_list


def move_zeros_3(lst):
    return list(sorted(lst, key=(lambda x: (x == 0))))


my_list = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros_3(my_list))
