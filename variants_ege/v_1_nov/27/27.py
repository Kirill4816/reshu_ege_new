# Набор данных состоит из пар натуральных чисел.
# Необходимо выбрать из каждой пары ровно одно число так,
# чтобы сумма всех выбранных чисел делилась на 3 и при этом была максимально возможной.

sum_num_2 = 0
min_dif = 20000
first = True
with open('A.txt', 'r') as file:
    for line in file.readlines():
        if first:
            first = False
            continue
        line = tuple(map(int, line.split()))
        if not line:
            continue
        max_num = max(line)
        sum_num_2 += max_num
        min_num = sum(line) - max_num
        cur_dif = max_num - min_num
        if cur_dif % 3 != 0:
            if cur_dif < min_dif:
                min_dif = cur_dif

if sum_num_2 % 3:
    print(sum_num_2)
else:
    print(sum_num_2 - min_dif)
