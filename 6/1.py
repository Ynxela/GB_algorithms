#! /usr/bin/env python
# -*- coding: utf-8 -*-

# wrapper
def return_var_size(func):
    import sys
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        all_vars = func.func_code.co_varnames
        sum_of_sizes = 0
        for var in all_vars:
            sum_of_sizes += sys.getsizeof(var)
        print('\x1b[1;36mпеременные {} : {} занимают {} байт\x1b[0;30m\n'.format(func.__name__, all_vars, sum_of_sizes))

    return wrapper


# 1
@return_var_size
def get_pos_char(num):
    position = 96
    letter = chr(num + position)
    print('Под номером {} находится буква {}'.format(num, letter))


# 2
@return_var_size
def check_leap_year(year):
    leap = 4
    leap100 = 100
    leap400 = 400
    if year % leap != 0:
        print('{} - не високосный год'.format(year))
    elif year % leap100 == 0:
        if year % leap400 == 0:
            print('{} - високосный год'.format(year))
        else:
            print('{} - не високосный год'.format(year))
    else:
        print('{} - високосный год'.format(year))


# 3
@return_var_size
def reverse_num(num):
    reverse = ''
    step = 1
    zero = 0
    a = str(num)
    idx = len(a) - step

    while idx >= zero:
        reverse += a[idx]
        idx -= step

    print('Перевернутое число = {}'.format(reverse))


get_pos_char(4)
check_leap_year(2019)
reverse_num(12345)

# python 3.6
# OS Ubuntu 18.04.02 64-bit
# Программы расположены по увеличению размера. Данные о размерах выводятся декоратором в консоль.
# Заметил особенность, что та же самая программа начинает занимать меньше места, если константы не определять в начале.
