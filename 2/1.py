'''
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа
не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.
'''

operator = ''
while operator != '0':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    while True:
        operator = input('Введите оператор ( + - * / ) или 0 для выхода: ')

        if operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/':
            if operator == '0':
                print('Программа завершена')
                break
        if operator == '/':
            if b == 0:
                print('Делить на 0 нельзя.')
                break
            result = a / b
            print('Результат деления равен {}'.format(result))
            break
        if operator == '+':
            result = a + b
            print('Результат сложения равен {}'.format(result))
            break
        if operator == '-':
            result = a - b
            print('Результат вычитания равен {}'.format(result))
            break
        result = a * b
        print('Результат умножения равен {}'.format(result))
        break