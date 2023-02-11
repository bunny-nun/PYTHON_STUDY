"""
Задание 27:
Пользователь вводит текст (строка). Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore, The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
"""
string = input('Введите строку: ')


def count_unique_words(input_string):
    print(set(input_string.lower().replace('. ', ' ').replace(', ',
                                                              ' ').split()))
    return len(set(input_string.lower().replace('. ',
                                                ' ').replace(', ',
                                                             ' ').split()))


print(count_unique_words(string))
