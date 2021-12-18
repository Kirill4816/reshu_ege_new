import math
with open('26 (2).txt', 'r') as file:
    first = True
    more_100_cnt = 0
    summ = 0
    most_expensive_with_sale = 0
    for line in file.readlines():
        if first:
            first = False
            continue
        num = int(line)
        if num > 100:
            more_100_cnt += 1
            if more_100_cnt % 2 == 0:
                if num > most_expensive_with_sale:
                    most_expensive_with_sale = num
                num *= 0.7

        summ += num

print(math.ceil(summ))
print(most_expensive_with_sale)
