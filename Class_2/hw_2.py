import fractions

"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с
числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

"""

frac1 = '1/2'
frac2 = '1/3'

frac1_lst = frac1.split('/')
frac2_lst = frac2.split('/')
for i in range(len(frac1_lst)):
    frac1_lst[i] = int(frac1_lst[i])

for i in range(len(frac2_lst)):
    frac2_lst[i] = int(frac2_lst[i])

total_sum = str((frac1_lst[0] * frac2_lst[1]) + (frac1_lst[1] * frac2_lst[0]))
total_sum += "/"
total_sum += str(frac1_lst[1] * frac2_lst[1])

total_mult = str(frac1_lst[0] * frac2_lst[0])
total_mult += "/"
total_mult += str(frac1_lst[1] * frac2_lst[1])

print(f'Сумма дробей: {total_sum}')
print(f'Произведение дробей: {total_mult}')

check_sum = fractions.Fraction(frac1) + fractions.Fraction(frac2)
check_mult = fractions.Fraction(frac1) * fractions.Fraction(frac2)
print(f'Сумма дробей: {check_sum}')
print(f'Произведение дробей: {check_mult}')
