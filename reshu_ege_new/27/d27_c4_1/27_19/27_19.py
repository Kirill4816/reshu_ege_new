with open('27_19.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

cnt_num_2_n_17 = 0
cnt_num_17_n_2 = 0
cnt_num_n_2_n_17 = 0

for number in numbers[1:]:
    if number % 2 == 0 and number % 17 != 0:
        cnt_num_2_n_17 += 1
    if number % 17 == 0 and number % 2 != 0:
        cnt_num_17_n_2 += 1
    if number % 17 != 0 and number % 2 != 0:
        cnt_num_n_2_n_17 += 1

cnt = cnt_num_2_n_17 * (cnt_num_2_n_17 - 1) // 2 + cnt_num_17_n_2 * (cnt_num_17_n_2 - 1) // 2 \
      + cnt_num_n_2_n_17 * (cnt_num_n_2_n_17 - 1) // 2 + cnt_num_2_n_17 * cnt_num_n_2_n_17 \
      + cnt_num_17_n_2 * cnt_num_n_2_n_17

print(cnt)
