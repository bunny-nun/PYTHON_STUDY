def is_pangram(s):
    import string
    for i in list(string.ascii_lowercase):
        if i not in s.lower():
            return False
    return True


# def is_pangram(s):
#     import string
#     return set(string.ascii_lowercase).issubset(s.lower())

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
