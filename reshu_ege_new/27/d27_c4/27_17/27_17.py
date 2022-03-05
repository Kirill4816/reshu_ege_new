with open('27_17.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

control_value = numbers[-1]
max_num_2 = 0
max_num_13 = 0
max_num_26 = 0
max_num = 0

for number in numbers[1:-1]:
    if number % 2 == 0 and number % 13 != 0 and number > max_num_2:
        max_num_2 = number
    if number % 13 == 0 and number > max_num_13 and number != max_num_2:
        max_num_13 = number
    if number % 26 == 0 and number > max_num_26:
        if max_num_26 > max_num:
            max_num = max_num_26
        max_num_26 = number
    elif number > max_num:
        max_num = number

res = max([max_num_2 * max_num_13, max_num_26 * max_num])

if res == control_value:
    print('Вычисленное контрольное значение:', res)
    print('Контроль пройден')
else:
    print('Вычисленное контрольное значение:', res)
    print('Контроль не пройден')
