with open('inf_26 (1).txt', 'r') as file:
    lines = file.readlines()

first = True
more_100_cnt = 0
sum_sale = 0
most_expensive_with_sale = 0
for line in lines:
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

    sum_sale += num

print(round(sum_sale))
print(most_expensive_with_sale)
