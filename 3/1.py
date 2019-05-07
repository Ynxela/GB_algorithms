# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

array = [i for i in range(2, 100)]

numbers = {i: 0 for i in range(2, 10)}

for number in numbers:
    for item in array:
        if item % number == 0:
            numbers[number] += 1

print(numbers)
