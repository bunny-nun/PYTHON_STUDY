"""
Задание № 3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.

"""

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
dct = iter({item: ord(item) for item in text}.items())

for _ in range(5):
    print(next(dct))