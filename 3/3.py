# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

import random

array = [random.randint(0, 100) for _ in range(10)]

min_el = array[0]
max_el = array[1]

for item in array:
    if item < min_el:
        min_el = item
    if item > max_el:
        max_el = item

idx_min = array.index(min_el)
idx_max = array.index(max_el)

print('\nold: ', array)

print('\n\nmin el: ', min_el, '\nmax el: ', max_el)

array[idx_max], array[idx_min] = array[idx_min], array[idx_max]

print('\n\nnew: ', array)
