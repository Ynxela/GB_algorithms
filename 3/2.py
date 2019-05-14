# Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
# 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

import random

array = [random.randint(0, 100) for _ in range(100)]

first_id = 0
last_id = len(array)

even_idx = []

for idx in range(first_id, last_id):
    if array[idx] % 2 == 0:
        even_idx.append(idx)

print(array, '\n\n', even_idx)
