import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    lesser = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


lst = [random.randint(0, 99) for i in range(20)]

print(lst)
print(quick_sort(lst))
