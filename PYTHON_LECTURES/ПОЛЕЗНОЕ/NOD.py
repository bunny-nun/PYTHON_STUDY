def method(a, b):
    if b == 0:
        return a
    print(f'a = {a}, b = {b}, % = {a % b}')
    return method(b, a % b)


method(36, 60)
