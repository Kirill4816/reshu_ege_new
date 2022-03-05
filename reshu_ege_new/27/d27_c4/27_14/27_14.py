with open('27_14.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

control_value = numbers[-1]
cnt_numbers = len(numbers[1:-1])
max_num_2_n_5 = 0
max_num_5_n_2 = 0
max_num_n_5_and_2 = 0

for number in numbers[1:-1]:
    prev_max_num_2_n_5 = 0
    prev_max_num_5_n_2 = 0
    prev_max_num_n_5_and_2 = 0
    if number % 2 == 0 and number % 5 != 0 and number > max_num_2_n_5:
        if max_num_2_n_5 > prev_max_num_2_n_5:
            prev_max_num_2_n_5 = max_num_2_n_5
        max_num_2_n_5 = number
    if number % 5 == 0 and number % 2 != 0 and number > max_num_5_n_2:
        if max_num_5_n_2 > prev_max_num_5_n_2:
            prev_max_num_5_n_2 = max_num_5_n_2
        max_num_5_n_2 = number
    if number % 5 != 0 and number % 2 != 0 and number > max_num_n_5_and_2:
        if max_num_n_5_and_2 > prev_max_num_n_5_and_2:
            prev_max_num_n_5_and_2 = max_num_n_5_and_2
        max_num_n_5_and_2 = number

res_1 = max_num_2_n_5 * prev_max_num_2_n_5
res_2 = max_num_5_n_2 * prev_max_num_5_n_2
res_3 = max_num_n_5_and_2 * prev_max_num_n_5_and_2
res_4 = max_num_n_5_and_2 * max_num_2_n_5
res_5 = max_num_n_5_and_2 * max_num_5_n_2

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
