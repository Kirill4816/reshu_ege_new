with open('27-B.txt', 'r') as file:
    numbers = file.readlines()

sum_even_1 = 0
sum_odd_2 = 0
sum_3_min = 0
min_dif = 10000
min_odd_min_dif = 0
first = True
for line in numbers:
    if first:
        first = False
        continue
    line = list(map(int, line.split()))
    min_num_line = min(line)
    sum_3_min += min_num_line
    line.remove(min_num_line)
    if line[0] % 2 == 0:
        sum_even_1 += line[0]
        sum_odd_2 += line[1]
    else:
        sum_odd_2 += line[0]
        sum_even_1 += line[1]
    if line[0] < line[1]:
        min_num_pair = line[0]
    else:
        min_num_pair = line[1]
    min_odd_min_dif = min_num_pair - min_num_line
    if min_odd_min_dif < min_dif:
        min_dif = min_odd_min_dif

if (sum_even_1 % 2 == 0 and sum_odd_2 % 2 == 0) or (sum_even_1 % 2 != 0 and sum_odd_2 % 2 != 0):
    sum_3_min += min_dif

print(sum_even_1, sum_odd_2, sum_3_min)
