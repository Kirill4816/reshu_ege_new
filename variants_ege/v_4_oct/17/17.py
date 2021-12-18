with open('17 (1).txt', 'r') as file:
    numbers = file.read().split()

numbers = map(int, numbers)
div_cnt = [0, 0, 0, 0, 0, 0, 0]
div_max = [0, 0, 0, 0, 0, 0, 0]
prev_max = 0
for num in numbers:
    modulo = num % 7
    div_cnt[modulo] += 1
    if modulo == 0:
        if div_max[0] < num:
            prev_max = div_max[0]
            div_max[0] = num
        elif prev_max < num:
            prev_max = num
    elif div_max[modulo] < num:
        div_max[modulo] = num
cnt = div_cnt[1] * div_cnt[6] + div_cnt[2] * div_cnt[5] + div_cnt[3] * div_cnt[4]
cnt += sum(tuple(range(div_cnt[0])))
sum_1 = div_max[0] + prev_max
sum_2 = div_max[1] + div_max[6]
sum_3 = div_max[2] + div_max[5]
sum_4 = div_max[3] + div_max[4]
max_sum = max((sum_1, sum_2, sum_3, sum_4))
print(cnt, max_sum)
