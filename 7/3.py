#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random

size = input('введите m и массив бует размером 2m+1: ')

array_1 = [random.randrange(-100, 100) for i in range(2 * size + 1)]

def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr

def find_media(arr):
    temp = gnome_sort(arr)

    median_index = len(arr) // 2

    return temp[median_index]

print(array_1)

print(find_media(array_1))