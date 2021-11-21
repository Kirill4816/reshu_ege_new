sum_num_3 = 0
min_dif = 20000
first = True
with open('A_2.txt', 'r') as file:
    for line in file.readlines():
        if first:
            first = False
            continue
        line = tuple(map(int, line.split()))
        if not line:
            continue
        max_num = max(line)
        sum_num_3 += max_num
        av_num = sum(line) - max_num - min(line)
        cur_dif = max_num - av_num
        if cur_dif % 109:
            if cur_dif < min_dif:
                min_dif = cur_dif

if sum_num_3 % 109 != 0:
    print(sum_num_3)
else:
    print(sum_num_3 - min_dif)
