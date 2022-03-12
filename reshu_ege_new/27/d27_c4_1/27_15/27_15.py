with open('27_15.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

control_value = numbers[-1]
cnt_numbers = len(numbers[1:-1])
max_num_3_n_5 = 0
max_num_5_n_3 = 0
max_num_n_5_and_3 = 0

for number in numbers[1:-1]:
    prev_max_num_3_n_5 = 0
    prev_max_num_5_n_3 = 0
    prev_max_num_n_5_and_3 = 0
    if number % 3 == 0 and number % 5 != 0 and number > max_num_3_n_5:
        if max_num_3_n_5 > prev_max_num_3_n_5:
            prev_max_num_3_n_5 = max_num_3_n_5
        max_num_3_n_5 = number
    if number % 5 == 0 and number % 3 != 0 and number > max_num_5_n_3:
        if max_num_5_n_3 > prev_max_num_5_n_3:
            prev_max_num_5_n_3 = max_num_5_n_3
        max_num_5_n_3 = number
    if number % 5 != 0 and number % 3 != 0 and number > max_num_n_5_and_3:
        if max_num_n_5_and_3 > prev_max_num_n_5_and_3:
            prev_max_num_n_5_and_3 = max_num_n_5_and_3
        max_num_n_5_and_3 = number

res_1 = max_num_3_n_5 * prev_max_num_3_n_5
res_2 = max_num_5_n_3 * prev_max_num_5_n_3
res_3 = max_num_n_5_and_3 * prev_max_num_n_5_and_3
res_4 = max_num_n_5_and_3 * max_num_3_n_5
res_5 = max_num_n_5_and_3 * max_num_5_n_3

res = max([res_1, res_2, res_3, res_4, res_5])

if res == control_value:
    print('Введено чисел:', cnt_numbers)
    print('Контрольное значение:', control_value)
    print('Вычисленное значение:', res)
    print('Значения совпали')
else:
    print('Введено чисел:', cnt_numbers)
    print('Контрольное значение:', control_value)
    print('Вычисленное значение:', res)
    print('Значения не совпали')
