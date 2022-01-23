# В текстовом файле записан набор натуральных чисел,
# не превышающих 108. Гарантируется, что все числа различны.
# Из набора нужно выбрать три числа, сумма которых делится на 3.
# Какую наибольшую сумму можно при этом получить?

with open('27-B (2).txt', 'r') as file:
    numbers = file.readlines()

# numbers = tuple(map(int, numbers[1:]))
# max_pair_nums_3 = 0
# len_numbers = len(numbers)
# for i in range(len_numbers):
#     for g in range(i + 1, len_numbers):
#         for j in range(g + 1, len_numbers):
#             sum_3 = numbers[i] + numbers[g] + numbers[j]
#             if sum_3 % 3 == 0:
#                 if sum_3 > max_pair_nums_3:
#                     max_pair_nums_3 = sum_3
# print(max_pair_nums_3)


numbers = tuple(map(int, numbers[1:]))
mod_1 = []
mod_2 = []
mod_0 = []
for num in numbers:
    if num % 3 == 0:
        mod_0.append(num)
    elif num % 3 == 2:
        mod_2.append(num)
    elif num % 3 == 1:
        mod_1.append(num)
mod_1.sort(reverse=True)
mod_2.sort(reverse=True)
mod_0.sort(reverse=True)
sum_1 = sum(mod_1[0:3])
sum_0 = sum(mod_0[0:3])
sum_2 = sum(mod_2[0:3])
sum_012 = mod_0[0] + mod_1[0] + mod_2[0]
print(max([sum_1, sum_2, sum_0, sum_012]))
