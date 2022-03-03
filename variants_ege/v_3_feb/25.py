from math import sqrt

cnt_num_M = 0
for number in range(10000001, 11000001):
    dividers = []
    for div in range(2, round(sqrt(number)) + 1):
        if number % div == 0:
            dividers.append(div)
            dividers.append(number // div)
    dividers.sort(reverse=True)
    if len(dividers) == 2:
        if sum(dividers) < 10000:
            print(sum(dividers))
            cnt_num_M += 1
            if cnt_num_M == 5:
                break
