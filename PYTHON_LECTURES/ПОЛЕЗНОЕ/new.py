my_generator = (x * x for x in range(3))
for i in my_generator:
    print(i)

for i in my_generator:  # генератор может использоваться только 1 раз
    print(i)

# лямбда-функция для списков
tables = [lambda x=x: x * 10 for x in range(1, 11)]
for table in tables:
    print(table())
