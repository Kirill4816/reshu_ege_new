with open('27_12.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_7 = 0
max_num_3 = 0
max_num_21 = 0
max_num = 0

for number in numbers[1:]:
    if number % 7 == 0 and number % 3 != 0 and number > max_num_7:
        max_num_7 = number
    if number % 3 == 0 and number > max_num_3 and number != max_num_7:
        max_num_3 = number
    if number % 21 == 0 and number > max_num_21:
        if max_num_21 > max_num:
            max_num = max_num_21
        max_num_21 = number
    elif number > max_num:
        max_num = number

res_1 = max_num_7 * max_num_3
res_2 = max_num * max_num_21

if res_1 % 21 != 0:
    res_1 = 0
if res_2 % 21 != 0:
    res_2 = 0

if res_1 > res_2 and res_1 != 0:
    print('Вычисленное контрольное значение:', res_1)
    print('Контроль пройден')
if res_2 > res_1 and res_2 != 0:
    print('Вычисленное контрольное значение:', res_2)
    print('Контроль пройден')
