with open('27_18.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

cnt_numbers = numbers[0]
cnt_num_2_n_26 = 0
cnt_num_13_n_26 = 0
cnt_num_26 = 0
max_num = 0

for number in numbers[1:]:
    if number % 2 == 0 and number % 26 != 0:
        cnt_num_2_n_26 += 1
    if number % 13 == 0 and number % 26 != 0:
        cnt_num_13_n_26 += 1
    if number % 26 == 0:
        cnt_num_26 += 1

# cnt = cnt_num_26 * (cnt_num_26 - 1) // 2 + cnt_num_26 * (cnt_numbers - cnt_num_26) + cnt_num_13_n_26 * cnt_num_2_n_26 почему так?

print(cnt)