"""
Find the missing letter
Write a method that takes an array of consecutive (increasing)
letters as input and that returns the missing letter in the array.

You will always get a valid array. And it will be always exactly one
letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""

letters = ['A', 'B', 'C', 'D', 'F']


def find_missing_letter(chars):
    # alphabet = [chr(i) for i in (range(65, 91))] + [chr(i) for i in
    #                                                 range(97, 123)]
    # return [alphabet[k] for k in
    #         range(alphabet.index(chars[0]), alphabet.index(chars[-1]) + 1) if
    #         alphabet[k] not in chars][0]

    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))


print(find_missing_letter(letters))
