"""
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid
decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3
will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0, 0, 0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

# конвертор в любую систему исчисления
# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits):
#         return None
#     result = str()
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result
#
#
# test = convert_to(255, 16, True)
#
# print(test)


def rgb(r, g, b):
    def to_hex(num):
        return min(255, max(num, 0))
    return f'{to_hex(r):02X}{to_hex(g):02X}{to_hex(b):02X}'


test = rgb(255, 255, 300)
print(test)
