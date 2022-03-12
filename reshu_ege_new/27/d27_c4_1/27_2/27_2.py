with open('27_2.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

min_num_3_0 = 1500
prev_min_num_3_0 = 1500
min_num_3_1 = 1500
min_num_3_2 = 1500

for number in numbers[1:]:
    if number % 3 == 0 and number < min_num_3_0:
        if min_num_3_0 < prev_min_num_3_0:
            min_num_3_0 = prev_min_num_3_0
        min_num_3_0 = number
    elif number % 3 == 0 and number < prev_min_num_3_0:
        prev_min_num_3_0 = number
    if number % 3 == 1 and number < min_num_3_1:
        min_num_3_1 = number
    if number % 3 == 2 and number < min_num_3_2:
        min_num_3_2 = number

res_1 = min_num_3_1 + min_num_3_2
res_2 = min_num_3_0 + prev_min_num_3_0

if res_1 % 3 != 0:
    res_1 = 1
if res_2 % 3 != 0:
    res_2 = 2

if res_1 < res_2 and res_1 != 1:
    print('Вычисленное контрольное значение:', res_1)
    print('Контроль пройден')
if res_2 < res_1 and res_2 != 1:
    print('Вычисленное контрольное значение:', res_2)
    print('Контроль пройден')
