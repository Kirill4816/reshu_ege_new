with open('27-B_2.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

max_num_2 = 0
max_num_7 = 0
max_num_14 = 0
max_num = 0

for number in numbers[1:]:
    cur_max_num = 0
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

print(max([max_num_2 * max_num_7, max_num_14 * max_num]))
