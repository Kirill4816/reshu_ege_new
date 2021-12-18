# Набор данных состоит из пар натуральных чисел.
# Необходимо выбрать из каждой пары ровно одно число так,
# чтобы сумма всех выбранных чисел делилась на 3 и при этом была максимально возможной.

sum_num_2 = 0
min_dif_2 = 20000
min_dif_1 = 20000
min_dif_1_2 = 20000
min_dif_2_2 = 20000
first = True
with open('B.txt', 'r') as file:
    for line in file.readlines():
        if first:
            first = False
            continue
        line = tuple(map(int, line.split()))
        max_num = max(line)
        sum_num_2 += max_num
        min_num = sum(line) - max_num
        cur_dif = max_num - min_num
        if cur_dif % 3 == 1:
            if cur_dif < min_dif_1:
                min_dif_1_2 = min_dif_1
                min_dif_1 = cur_dif
            elif cur_dif < min_dif_1_2:
                min_dif_1_2 = cur_dif

        if cur_dif % 3 == 2:
            if cur_dif < min_dif_2:
                min_dif_2_2 = min_dif_2
                min_dif_2 = cur_dif
            elif cur_dif < min_dif_2_2:
                min_dif_2_2 = cur_dif


if sum_num_2 % 3 == 0:
    print(sum_num_2)
elif sum_num_2 % 3 == 1:
    if min_dif_1 < min_dif_2 + min_dif_2_2:
        print(sum_num_2 - min_dif_1)
    else:
        print(sum_num_2 - min_dif_2 - min_dif_2_2)
else:
    if min_dif_2 < min_dif_1 + min_dif_1_2:
        print(sum_num_2 - min_dif_2)
    else:
        print(sum_num_2 - min_dif_1 - min_dif_1_2)

