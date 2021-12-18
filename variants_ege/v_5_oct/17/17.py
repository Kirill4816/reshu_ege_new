with open('17 (2).txt', 'r') as file:
    numbers = file.read().split()

numbers = map(int, numbers)
cnt_26 = 0
cnt_2 = 0
cnt_13 = 0
max_26 = 0
max_13 = 0
max_2 = 0
max_num = 0
cnt_numbers = 0
for num in numbers:
    cur = False
    if num % 26 == 0:
        cnt_26 += 1
        if num > max_26:
            max_26 = num
            cur = True
    elif num % 13 == 0:
        cnt_13 += 1
        if num > max_13:
            max_13 = num
    elif num % 2 == 0:
        cnt_2 += 1
        if num > max_2:
            max_2 = num
    cnt_numbers += 1
    if num > max_num and cur is False:
        max_num = num
cnt = cnt_2 * cnt_13 + sum(tuple(range(cnt_numbers - 1, cnt_numbers - cnt_26 - 1, - 1)))
print(cnt)
sum_2_13 = max_2 + max_13
sum_26_max = max_26 + max_num
if sum_2_13 > sum_26_max:
    print(sum_2_13)
else:
    print(sum_26_max)


