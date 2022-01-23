# В текстовом файле записан набор натуральных чисел,
# не превышающих 109. Гарантируется, что все числа различны.
# Необходимо определить, сколько в наборе таких пар чётных чисел,
# что их среднее арифметическое тоже присутствует в файле,
# и чему равно наибольшее из средних арифметических таких пар.
# В текстовом файле записан набор натуральных чисел,
# не превышающих 109. Гарантируется, что все числа различны.
# Необходимо определить, сколько в наборе таких пар чётных чисел,
# что их среднее арифметическое тоже присутствует в файле,
# и чему равно наибольшее из средних арифметических таких пар.

with open('26 (3).txt', 'r') as file:
    numbers = file.readlines()

numbers = tuple(map(int, numbers[1:]))
cnt_pair = 0
max_cnt_pair = 0
odd_numbers = [num for num in numbers if num % 2 == 0]
len_numbers = len(odd_numbers)
for i in range(len_numbers):
    for g in range(i + 1, len_numbers):
        average_pair = (odd_numbers[i] + odd_numbers[g]) // 2
        if average_pair in numbers:
            print(average_pair)
            cnt_pair += 1
            if average_pair > max_cnt_pair:
                max_cnt_pair = average_pair
print(cnt_pair, max_cnt_pair)
