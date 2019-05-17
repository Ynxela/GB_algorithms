# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


class SixteenNums():

    def __init__(self, number):
        self.number = list(number.upper())
        self.num_len = len(number)

    def __add__(self, second_num):
        c = None
        deq = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'])
        second_num_len = len(second_num)

        if self.num_len > second_num_len:
            c = self.number.copy()
        else:
            c = second_num.copy()

        for num in range(0, len(c), -1):
            pass

    def __str__(self):
        return str(self.number)

    def __len__(self):
        return len(self.number)

    def copy(self):
        return self.number

a = SixteenNums(input('Введите 1 16-ричное число: '))
b = SixteenNums(input('Введите 2 16-ричное число: '))

print(a, b)

print(a + b)
