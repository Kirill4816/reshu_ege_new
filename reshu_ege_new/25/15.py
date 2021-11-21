# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [568023; 569230],
# число, имеющее максимальное количество различных натуральных делителей,
# если таких чисел несколько — найдите минимальное из них.
# Выведите на экран количество делителей такого числа и само число.

first_number = 568023
second_number = 569230
max_cnt_dividers = 0
max_cnt_div_number = 0

for number in range(first_number, second_number + 1):
    cur_cnt_dividers = 1
    for divider in range(1, second_number // 2 + 1):
        if number % divider == 0:
            cur_cnt_dividers += 1
    if cur_cnt_dividers > max_cnt_dividers:
        max_cnt_dividers = cur_cnt_dividers
        max_cnt_div_number = number

print(max_cnt_dividers, max_cnt_div_number)
