with open('27_21.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

cnt_numbers = numbers[0]
cnt_num_62 = 0
cnt_num_31_n_62 = 0
cnt_num_2_n_62 = 0

for number in numbers[1:]:
    if number % 62 == 0:
        cnt_num_62 += 1
    if number % 31 == 0 and number % 62 != 0:
        cnt_num_31_n_62 += 1
    if number % 2 == 0 and number % 62 != 0:
        cnt_num_2_n_62 += 1

cnt = cnt_num_62 * (cnt_num_62 - 1) // 2 + cnt_num_62 * (cnt_numbers - cnt_num_62)\
      + cnt_num_2_n_62 * cnt_num_31_n_62

print(cnt)
