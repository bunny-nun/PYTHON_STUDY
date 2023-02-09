import random


def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]
        merge_sort(left_array)
        merge_sort(right_array)
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

    return array


lst = [random.randint(0, 99) for i in range(20)]

print(lst)
print(merge_sort(lst))
