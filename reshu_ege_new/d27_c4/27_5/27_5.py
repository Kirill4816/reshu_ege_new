with open('27_5.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_2 = 0
max_num_7 = 0
max_num_14 = 0
max_num = 0

for number in numbers[1:]:
    if number % 2 == 0 and number % 7 != 0 and number > max_num_2:
        max_num_2 = number
    if number % 7 == 0 and number > max_num_7 and number != max_num_2:
        max_num_7 = number
    if number % 14 == 0 and number > max_num_14:
        if max_num_14 > max_num:
            max_num = max_num_14
        max_num_14 = number
    elif number > max_num:
        max_num = number

res_1 = max_num_2 * max_num_7
res_2 = max_num * max_num_14

if res_1 % 14 != 0:
    res_1 = 0
if res_2 % 14 != 0:
    res_2 = 0

if res_1 > res_2 and res_1 != 0:
    print('Вычисленное контрольное значение:', res_1)
    print('Контроль пройден')
if res_2 > res_1 and res_2 != 0:
    print('Вычисленное контрольное значение:', res_2)
    print('Контроль пройден')
