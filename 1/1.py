a = int(input('введите 3-х значное число: '))
a3 = a // 100
a2 = (a - a3 * 100) // 10
a1 = a - a3 * 100 - a2 * 10
sum3 = a1 + a2 + a3
comp3 = a1 * a2 * a3
print('сумма цифр = {}'.format(sum3))
print('произведение цифр = {}'.format(comp3))
