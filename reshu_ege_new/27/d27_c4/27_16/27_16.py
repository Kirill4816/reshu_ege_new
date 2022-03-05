with open('27_16.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

control_value = numbers[-1]
min_num_2 = 1200
min_num_3 = 1200
min_num_6 = 1200
min_num = 1200

for number in numbers[1:-1]:
    if number % 2 == 0 and number % 3 != 0 and number < min_num_2:
        min_num_2 = number
    if number % 3 == 0 and number < min_num_3 and number != min_num_2:
        min_num_3 = number
    if number % 6 == 0 and number < min_num_6:
        if min_num_6 < min_num:
            min_num = min_num_6
        min_num_6 = number
    elif number < min_num:
        min_num = number

res_1 = min_num_2 * min_num_3
res_2 = min_num * min_num_6

if res_1 % 6 != 0:
    res_1 = 0
if res_2 % 6 != 0:
    res_2 = 0

if res_1 < res_2 and res_1 != 0:
    if res_1 == control_value:
        print('Вычисленное контрольное значение:', res_1)
        print('Контроль пройден')
    else:
        print('Вычисленное контрольное значение:', res_1)
        print('Контроль не пройден')
if res_2 < res_1 and res_2 != 0:
    if res_2 == control_value:
        print('Вычисленное контрольное значение:', res_2)
        print('Контроль пройден')
    else:
        print('Вычисленное контрольное значение:', res_2)
        print('Контроль не пройден')
