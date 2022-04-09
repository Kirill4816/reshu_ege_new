sum_max_num_3 = 0
min_dif_1 = float('inf')
min_dif_2 = float('inf')
min_dif_1_2 = float('inf')
min_dif_2_2 = float('inf')
first = True

with open('inf_22_10_20_27b.txt', 'r') as file:
    for line in file.readlines():
        if first:
            first = False
            continue
        line = tuple(map(int, line.split()))
        max_num = max(line)
        sum_max_num_3 += max_num
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

if sum_max_num_3 % 3 == 0:
    print(sum_max_num_3)
elif sum_max_num_3 % 3 == 1:
    if min_dif_1 < min_dif_2 + min_dif_2_2:
        print(sum_max_num_3 - min_dif_1)
    else:
        print(sum_max_num_3 - min_dif_2 - min_dif_2_2)
elif sum_max_num_3 % 3 == 2:
    if min_dif_2 < min_dif_1 + min_dif_1_2:
        print(sum_max_num_3 - min_dif_2)
    else:
        print(sum_max_num_3 - min_dif_1 - min_dif_1_2)
