"""
Create a function taking a positive integer between 1 and 3999 (both included)
as its parameter and returning a string containing the Roman Numeral
representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""


def solution(n):
    symbols = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10),
               ('V', 5), ('I', 1), ('', 1)]
    roman = str()
    for i in range(len(symbols) - 1):
        if n / symbols[i][1] > 0:
            if n // symbols[i][1] > 3:
                roman += symbols[i][0] + symbols[i - 1][0]
                n += symbols[i][1] - symbols[i - 1][1]
            if i % 2 != 0 and (n - symbols[i][1]) // symbols[i + 1][1] > 3:
                roman += symbols[i + 1][0] + symbols[i - 1][0]
                n += symbols[i + 1][1] - symbols[i - 1][1]
            else:
                roman += symbols[i][0] * (n // symbols[i][1])
                n -= symbols[i][1] * (n // symbols[i][1])
    return roman


def solution_2(n):
    symbols = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
               ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
               ('V', 5), ('IV', 4), ('I', 1)]
    roman = str()
    for i in symbols:
        roman += i[0] * (n // i[1])
        n -= i[1] * (n // i[1])
    return roman


number = 89
print(solution_2(number))
