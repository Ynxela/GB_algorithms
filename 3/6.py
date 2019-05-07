# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.
import random

array = [random.randint(0, 100) for _ in range(10)]
sum_min_max = 0

min_el = array[0]
max_el = array[1]

for item in array:
    if item < min_el:
        min_el = item
    if item > max_el:
        max_el = item

for i in range(min_el + 1, max_el):
    sum_min_max += i

print('\narray: ', array)
print('\n\nmin el: ', min_el, '\nmax el: ', max_el)
print('\n\nсумма элементов: ', sum_min_max)
