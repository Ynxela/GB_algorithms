# Определить, какое число в массиве встречается чаще всего


import random
import timeit
import cProfile

# 1 вариант - скопированное решение 4 задачи из 3 урока.

a = """numbers = {}

max_number = 0
max_quantity = 0

array = [random.randint(0, 50) for _ in range(100000)]

for item in array:
    if item in numbers:
        numbers[item] += 1
    else:
        numbers[item] = 1

for key, value in numbers.items():
    if value > max_quantity:
        max_quantity = value
        max_number = key

print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))"""


def main_1():
    numbers = {}

    max_number = 0
    max_quantity = 0

    array = [random.randint(0, 50) for _ in range(1000000)]

    for item in array:
        if item in numbers:
            numbers[item] += 1
        else:
            numbers[item] = 1

    for key, value in numbers.items():
        if value > max_quantity:
            max_quantity = value
            max_number = key

    print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))


# print(timeit.timeit(a, number=100, globals=globals()))
# timeit:
# 0.011066037986893207 - для _ in range 100
# 0.08638163097202778 - для _ in range 1000
# 0.8553230999968946 - для _ in range 10000
# 8.300402263994329 - для _ in range 100000

# cProfile - для _ in range 1000000
# cProfile.run('main_1()')
# 5254901 function calls in 1.431 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.071    0.071    1.430    1.430 4.py:32(main_1)
#         1    0.157    0.157    1.358    1.358 4.py:38(<listcomp>)
#         1    0.001    0.001    1.431    1.431 <string>:1(<module>)
#   1000000    0.444    0.000    0.982    0.000 random.py:173(randrange)
#   1000000    0.220    0.000    1.202    0.000 random.py:217(randint)
#   1000000    0.383    0.000    0.538    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    1.431    1.431 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1000000    0.049    0.000    0.049    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#   1254893    0.105    0.000    0.105    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# 2 вариант - нахождение числа сразу в цикле

b = """numbers = {}

max_number = 0
max_quantity = 0

array = [random.randint(0, 50) for _ in range(100000)]

for item in array:
    if item in numbers:
        numbers[item] += 1
    else:
        numbers[item] = 1
    if numbers[item] > max_quantity:
        max_quantity = numbers[item]
        max_number = item

print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))"""


def main_2():
    numbers = {}

    max_number = 0
    max_quantity = 0

    array = [random.randint(0, 50) for _ in range(1000000)]

    for item in array:
        if item in numbers:
            numbers[item] += 1
        else:
            numbers[item] = 1
        if numbers[item] > max_quantity:
            max_quantity = numbers[item]
            max_number = item

    print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))


# print(timeit.timeit(b, number=100, globals=globals()))
# timeit:
# 0.009158316010143608 - для _ in range 100
# 0.09677379601635039 - для _ in range 1000
# 0.8925127869588323 - для _ in range 10000
# 8.669438162003644 - для _ in range 100000

# cProfile - для _ in range 1000000
# cProfile.run('main_2()')
# 5253692 function calls in 1.421 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.101    0.101    1.420    1.420 4.py:102(main_2)
#         1    0.159    0.159    1.319    1.319 4.py:108(<listcomp>)
#         1    0.001    0.001    1.421    1.421 <string>:1(<module>)
#   1000000    0.437    0.000    0.959    0.000 random.py:173(randrange)
#   1000000    0.202    0.000    1.160    0.000 random.py:217(randint)
#   1000000    0.366    0.000    0.522    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    1.421    1.421 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1000000    0.051    0.000    0.051    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#   1253685    0.104    0.000    0.104    0.000 {method 'getrandbits' of '_random.Random' objects}

# 3 вариант - использование функции max()

def main_3():
    numbers = {}

    max_number = 0

    array = [random.randint(0, 50) for _ in range(1000000)]

    for item in array:
        if item in numbers:
            numbers[item] += 1
        else:
            numbers[item] = 1

    max_quantity = max(numbers.values())
    for key, value in numbers.items():
        if value == max_quantity:
            max_number = key

    print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))

c = """numbers = {}

max_number = 0

array = [random.randint(0, 50) for _ in range(100000)]

for item in array:
    if item in numbers:
        numbers[item] += 1
    else:
        numbers[item] = 1

max_quantity = max(numbers.values())
for key, value in numbers.items():
    if value == max_quantity:
        max_number = key

print('число {0} встретилось {1} раз.'.format(max_number, max_quantity))"""

# print(timeit.timeit(c, number=100, globals=globals()))
# timeit:
# 0.009478038002271205 - для _ in range 100
# 0.09253385500051081 - для _ in range 1000
# 0.8674788940115832 - для _ in range 10000
# 8.513573699980043 - для _ in range 100000

# cProfile - для _ in range 1000000
# cProfile.run('main_3()')
# 5254485 function calls in 1.386 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.073    0.073    1.385    1.385 4.py:151(main_3)
#         1    0.156    0.156    1.312    1.312 4.py:156(<listcomp>)
#         1    0.001    0.001    1.386    1.386 <string>:1(<module>)
#   1000000    0.433    0.000    0.953    0.000 random.py:173(randrange)
#   1000000    0.203    0.000    1.156    0.000 random.py:217(randint)
#   1000000    0.363    0.000    0.520    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    1.386    1.386 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1000000    0.051    0.000    0.051    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#   1254475    0.106    0.000    0.106    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#         1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}

# Вывод: Во всех трех случаях скорость вычислений равнялась примерно O(n). То есть, при учеличении входящих данных
# в 10 раз, скоротьь вычислений уменьшалась так же в 10 раз. Самым быстрым оказался 1 алгоритм, если судить по timeit
# Если брать cProfile, то в этом случае - 3 алгоритм.