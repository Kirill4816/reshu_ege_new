with open('17.txt', 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
cnt_n_34 = 0
cnt_n_17 = 0
cnt_n_2 = 0
max_n_34 = 0
max_n_17 = 0
max_n_2 = 0
max_sum = 0
cnt_numbers = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] * numbers[j] % 34 != 0:
            cnt_n_34 += 1
            if numbers[i] + numbers[j] > max_sum:
                max_sum = numbers[i] + numbers[j]
print(cnt_n_34, max_sum)
    # cur = False
    # if num % 34:
    #     cnt_n_34 += 1
    #     if num > max_n_34:
    #         max_n_34 = num
    #         cur = True
    # if num % 17:
    #     cnt_n_17 += 1
    #     if num > max_n_17:
    #         max_n_17 = num
    # elif num % 2:
    #     cnt_n_2 += 1
    #     if num > max_n_2:
    #         max_n_2 = num
    # cnt_numbers += 1
    # if num > max_num and cur is False:
    #     max_num = num
# print(cnt_n_2, cnt_n_17)
# cnt = cnt_n_2 * cnt_n_17 + sum(tuple(range(cnt_numbers - 1, cnt_numbers - cnt_n_34 - 1, - 1)))
# print(cnt)
# sum_n_2_17 = max_n_2 + max_n_17
# sum_n_34_max = max_n_34 + max_num
# if sum_n_2_17 > sum_n_34_max:
#     print(sum_n_2_17)
# else:
#     print(sum_n_34_max)
