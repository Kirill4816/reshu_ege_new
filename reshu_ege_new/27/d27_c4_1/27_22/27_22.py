with open('27_22.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

cnt_numbers = numbers[0]
cnt_num_5_n_10 = 0
cnt_num_2_n_10 = 0
cnt_num_10 = 0

for number in numbers[1:]:
    if number % 5 == 0 and number % 10 != 0:
        cnt_num_5_n_10 += 1
    if number % 2 == 0 and number % 10 != 0:
        cnt_num_2_n_10 += 1
    if number % 10 == 0:
        cnt_num_10 += 1

cnt = cnt_num_10 * (cnt_num_10 - 1) // 2 + cnt_num_10 * (cnt_numbers - cnt_num_10) \
      + cnt_num_2_n_10 * cnt_num_5_n_10

print(cnt)
