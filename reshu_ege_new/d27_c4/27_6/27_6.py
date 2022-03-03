with open('27_6.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_2 = 0
max_num_5 = 0
max_num_10 = 0
max_num = 0

for number in numbers[1:]:
    if number % 2 == 0 and number % 5 != 0 and number > max_num_2:
        max_num_2 = number
    if number % 5 == 0 and number > max_num_5 and number != max_num_2:
        max_num_5 = number
    if number % 10 == 0 and number > max_num_10:
        if max_num_10 > max_num:
            max_num = max_num_10
        max_num_10 = number
    elif number > max_num:
        max_num = number

res_1 = max_num_2 * max_num_5
res_2 = max_num * max_num_10

if res_1 % 10 != 0:
    res_1 = 0
if res_2 % 10 != 0:
    res_2 = 0

if res_1 > res_2 and res_1 != 0:
    print('Вычисленное контрольное значение:', res_1)
    print('Контроль пройден')
if res_2 > res_1 and res_2 != 0:
    print('Вычисленное контрольное значение:', res_2)
    print('Контроль пройден')
