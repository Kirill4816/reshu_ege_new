# В текстовом файле записан набор натуральных чисел,
# не превышающих 108. Гарантируется, что все числа различны.
# Из набора нужно выбрать три числа, сумма которых делится на 3.
# Какую наибольшую сумму можно при этом получить?

with open('27-A (2).txt', 'r') as file:
    numbers = file.readlines()

numbers = tuple(map(int, numbers[1:]))
max_pair_nums_3 = 0
len_numbers = len(numbers)
for i in range(len_numbers):
    for g in range(i + 1, len_numbers):
        for j in range(g + 1, len_numbers):
            sum_3 = i + g + j
            if sum_3 % 3 == 0:
                if sum_3 > max_pair_nums_3:
                    max_pair_nums_3 = sum_3
print(max_pair_nums_3)
