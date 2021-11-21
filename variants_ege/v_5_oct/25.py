first_number = 84052
second_number = 84130
max_cnt_div = 0
nums_with_max_cnt_of_divisors = []
for number in range(first_number, second_number + 1):
    cur_cnt_div = 1
    for divider in range(1, number // 2 + 1):
        if number % divider == 0:
            cur_cnt_div += 1
    if cur_cnt_div > max_cnt_div:
        max_cnt_div = cur_cnt_div
        nums_with_max_cnt_of_divisors = [number]
    elif cur_cnt_div == max_cnt_div:
        nums_with_max_cnt_of_divisors.append(number)

nums_with_max_cnt_of_divisors.sort()

print(max_cnt_div, nums_with_max_cnt_of_divisors[0])
