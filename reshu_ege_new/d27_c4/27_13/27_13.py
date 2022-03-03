with open('27_13.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_n_7 = 0
max_num_7_n_49 = 0

for number in numbers[1:]:
    if number % 7 == 0 and number % 49 != 0 and number > max_num_7_n_49:
        max_num_7_n_49 = number
    if number % 7 != 0 and number > max_num_n_7:
        max_num_n_7 = number

res = max_num_n_7 * max_num_7_n_49


if res % 7 != 0 or res % 49 == 0:
    res = 1
    print('Вычисленное контрольное значение:', res)
    print('Контроль не пройден')

if res % 7 == 0 and res % 49 != 0:
    print('Вычисленное контрольное значение:', res)
    print('Контроль пройден')
