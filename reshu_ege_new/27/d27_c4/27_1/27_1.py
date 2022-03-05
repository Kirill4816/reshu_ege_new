with open('27_1.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_3_0 = 0
prev_max_num_3_0 = 0
max_num_3_1 = 0
max_num_3_2 = 0

for number in numbers[1:]:
    if number % 3 == 0 and number > max_num_3_0:
        if max_num_3_0 > prev_max_num_3_0:
            max_num_3_0 = prev_max_num_3_0
        max_num_3_0 = number
    elif number % 3 == 0 and number > prev_max_num_3_0:
        prev_max_num_3_0 = number
    if number % 3 == 1 and number > max_num_3_1:
        max_num_3_1 = number
    if number % 3 == 2 and number > max_num_3_2:
        max_num_3_2 = number

res_1 = max_num_3_1 + max_num_3_2
res_2 = max_num_3_0 + prev_max_num_3_0

if res_1 % 3 != 0:
    res_1 = 1
if res_2 % 3 != 0:
    res_2 = 1

if res_1 > res_2 and res_1 != 1:
    print('Вычисленное контрольное значение:', res_1)
    print('Контроль пройден')
if res_2 > res_1 and res_2 != 1:
    print('Вычисленное контрольное значение:', res_2)
    print('Контроль пройден')
