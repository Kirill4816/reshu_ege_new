with open('27_20.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

cnt_numbers = numbers[0]
cnt_num_2_n_7 = 0
cnt_num_7_n_2 = 0
cnt_num_14 = 0

for number in numbers[1:]:
    if number % 2 == 0 and number % 7 != 0:
        cnt_num_2_n_7 += 1
    if number % 7 == 0 and number % 2 != 0:
        cnt_num_7_n_2 += 1
    if number % 14 == 0:
        cnt_num_14 += 1

cnt = cnt_numbers * (cnt_numbers - 1) // 2 - cnt_num_14 * (cnt_numbers - cnt_num_14)\
      - cnt_num_14 * (cnt_num_14 - 1) // 2 - cnt_num_2_n_7 * cnt_num_7_n_2

print(cnt)
