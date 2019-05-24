# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее)
import random


def bubble_sort(array):
    n = 1
    sort = False
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sort = True
        if not sort:
            break
        n += 1

    return array


array_1 = [random.randrange(-100, 100) for i in range(10)]

print('unsorted:', array_1)

array_1 = bubble_sort(array_1)

print('sorted:', array_1)
