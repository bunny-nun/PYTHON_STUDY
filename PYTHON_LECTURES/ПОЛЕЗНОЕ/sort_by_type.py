a = [1, 2, 3, 'a', 4, 'b', '123']


#
# def filter_list(my_list):
#     new_list = []
#     for i in my_list:
#         if str(i).isdigit():
#             new_list.append(i)
#     return new_list
#
#
# print(filter_list(a))


def filter_list02(my_list):
    """return a new list with the strings filtered out"""
    return [i for i in my_list if str(i).isdigit()]


print(filter_list02(a))


def filter_list03(my_list):
    """return only int elements"""
    return [i for i in my_list if isinstance(i, int)]
    # return [i for i in my_list if type(i) is int]


print(filter_list03(a))


def filter_list04(my_list):
    """return a new list with sorted by int type"""
    return [sorted(my_list, key=lambda i: str(i).isdigit())]


print(filter_list04(a))


def filter_list04(my_list):
    """return only int elements"""
    return [i for i in my_list if isinstance(i, int)]
    # return [i for i in my_list if type(i) is int]


print(filter_list04(a))