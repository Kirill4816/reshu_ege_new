with open('17.txt', 'r') as file:
    cnt_num_10 = 0
    cnt_num_5 = 0
    cnt_num_2 = 0
    cnt_num = 0
    max_num_10 = 0
    max_num = 0
    max_num_5 = 0
    max_num_2 = 0
    max_num_10_cnt = 1
    for number in file.readlines():
        number = int(number)
        cnt_num += 1
        if number == max_num_10:
            max_num_10_cnt += 1
        if number % 10 == 0:
            cnt_num_10 += 1
            if number > max_num_10:
                max_num_10 = number
                max_num_10_cnt = 1
        elif number % 2 == 0:
            cnt_num_2 += 1
            if number > max_num_2:
                max_num_2 = number
        elif number % 5 == 0:
            cnt_num_5 += 1
            if number > max_num_5:
                max_num_5 = number
        if number > max_num:
            if number == max_num_10 and max_num_10_cnt < 2:
                continue
            max_num = number
    cnt = 0
    for i in range(1, cnt_num_10 + 1):
        cnt += cnt_num - i
    pairs_cnt = cnt_num_2 * cnt_num_5 + cnt
    print(pairs_cnt)
    sum_1 = max_num_5 + max_num_2
    sum_2 = max_num_10 + max_num
    if sum_1 > sum_2:
        print(sum_1)
    else:
        print(sum_2)

    print(cnt_num_5)
    print(cnt_num_2)
    print(cnt_num_10)
    print(cnt_num)