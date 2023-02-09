def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


lst = list()
for i in range(1, 10):
    lst.append(fibonacci(i))
print(lst)
