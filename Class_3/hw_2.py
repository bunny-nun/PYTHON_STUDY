"""
В большой текстовой строке text подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами, апостроф не считается за пробел. Такие слова как
dont, its, didnt итд (после того, как убрали знак препинания апостроф) считать одним словом.

[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

"""

text = 'Hello world. Hello Python. Hello again. five six seven eight nine ten eleven eleven'

text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

"""
[('and', 3), ('python', 2), ('language', 2), ('code', 2), ('its', 2), ('is', 1), ('an', 1), ('interpreted', 1), ('high', 1), ('level', 1)]
"""

text = "Python 3.9 is the latest version of Python. It's awesome!"

"""
[('python', 2), ('is', 1), ('the', 1), ('latest', 1), ('version', 1), ('of', 1), ('it', 1), ('s', 1), ('awesome', 1)]
"""


text = text.lower()
for item in text:
    if not item.isalpha():
        text = text.replace(item, " ")
text = ' '.join(text.split())

lst = text.split(" ")
dct = {}

for item in lst:
    dct[item] = dct.get(item, 0) + 1

res = sorted(dct.items(), key=lambda x: x[1], reverse=True)[:10]

print(res)
