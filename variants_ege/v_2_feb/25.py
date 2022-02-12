num = 452022
cnt_num_M = 0
while cnt_num_M < 5:
    for div in range(2, num // 2 + 1):
        if num % div == 0:
            M = div + num // div
    if M % 7 == 3:
        print(num, M)
        cnt_num_M += 1
    num += 1
