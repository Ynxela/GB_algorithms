#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import OrderedDict


class SixteenNums():

    def __init__(self, number):
        self.number = list(number.upper())

    def __add__(self, second_num):
        weights = OrderedDict({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                               'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '10': 'A', '11': 'B', '12': 'C', '13': 'D',
                               '14': 'E', '15': 'F'})
        tmp = 0
        result_num = []
        result = ''

        # Создаем вспомогательные списки на основе имеющихся объектов
        if len(self) > len(second_num):
            c = self.reverse()
            d = second_num.reverse()
        else:
            c = second_num.reverse()
            d = self.reverse()

        for num in range(0, len(c)):
            try:
                res = weights[c[num]] + weights[d[num]] + tmp
            except IndexError:
                res = weights[c[num]] + tmp
            if res > 15:
                res -= 16
                tmp = 1
            else:
                tmp = 0
            result_num.append(str(weights[str(res)]))
            if num == len(c) - 1 and tmp == 1:
                result_num.append(str(tmp))

        result_num = result_num[::-1]

        for num in result_num:
            result += num

        return SixteenNums(result)

    def __str__(self):
        return str(self.number)

    def __len__(self):
        return len(self.number)

    def reverse(self):
        return self.number[::-1]


a = SixteenNums(input('Введите 1 16-ричное число: '))
b = SixteenNums(input('Введите 2 16-ричное число: '))

print('\na + b =', a + b, '\n')
print('a + b + a + b =', a + b + a + b)
