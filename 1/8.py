a = int(input('введите год: '))
if a % 4 != 0:
    print('{} - не високосный год'.format(a))
elif a % 100 == 0:
    if a % 400 == 0:
        print('{} - високосный год'.format(a))
    else:
        print('{} - не високосный год'.format(a))
else:
    print('{} - високосный год'.format(a))