# Определить, какое число в массиве встречается чаще всего

import random
from pprint import pprint

numbers = {}

max_number = 0
max_quantity = 0

array = [random.randint(0, 50) for _ in range(100)]

for item in array:
    if item in numbers:
        numbers[item] += 1
    else:
        numbers[item] = 1

for key, value in numbers.items():
    if value > max_quantity:
        max_quantity = value
        max_number = key

pprint(numbers)
print('\n\nчисло {0} встретилось {1} раз.'.format(max_number, max_quantity))
