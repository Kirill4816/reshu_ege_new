with open('27_1.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers[1:]))
cnt = 0
cnt_even_3 = 0
cnt_odd_3 = 0
cnt_even_n_3 = 0
cnt_odd_n_3 = 0
for number in numbers:
    if number % 2 == 0:
        if number % 3 == 0:
            cnt_even_3 += 1
        else:
            cnt_even_n_3 += 1
    else:
        if number % 3 != 0:
            cnt_odd_3 += 1
        else:
            cnt_odd_n_3 += 1

cnt = cnt_even_3 * cnt_odd_3 + cnt_even_n_3 * cnt_odd_3 + cnt_even_3 * cnt_odd_n_3

print(cnt)
