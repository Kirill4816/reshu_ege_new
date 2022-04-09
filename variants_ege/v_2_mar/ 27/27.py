with open('27-A (6).txt', 'r') as file:
    numbers = file.readlines()

sum_even_1 = 0
sum_odd_2 = 0
sum_3_max = 0
min_odd_dif_1 = 10001
min_odd_dif_2 = 10001
first = True
for line in numbers:
    if first:
        first = False
        continue
    line = list(map(int, line.split()))
    max_num_line = max(line)
    sum_3_max += max_num_line
    line.remove(max_num_line)
    sum_even_1 += line[0]
    sum_odd_2 += line[1]
    cur_dif_1 = abs(max_num_line - line[0])
    if cur_dif_1 % 2 != 0 and cur_dif_1 < min_odd_dif_1:
        min_odd_dif_1 = cur_dif_1

    cur_dif_2 = abs(max_num_line - line[1])
    if cur_dif_2 % 2 != 0 and cur_dif_2 < min_odd_dif_2:
        min_odd_dif_2 = cur_dif_2

if sum_even_1 % 2 == 0 and sum_odd_2 % 2 == 0:
    sum_3_max -= min_odd_dif_2
elif sum_even_1 % 2 != 0 and sum_odd_2 % 2 != 0:
    sum_3_max -= min_odd_dif_1

print(sum_3_max)
