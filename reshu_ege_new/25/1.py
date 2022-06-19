from math import sqrt

num_max_sum_div = []
flag = True
num = 10000000

while len(num_max_sum_div) < 5:
    num += 1
    dividers = []
    for div in range(2, round(sqrt(num))):
        if num % div == 0:
            dividers.append(div)
            div_2 = num // div
            if div_2 not in dividers:
                dividers.append(div_2)
    if len(dividers) < 2:
        continue
    dividers.sort(reverse=True)
    sum_div = dividers[0] + dividers[1]
    if 0 < sum_div < 10000:
        num_max_sum_div.append(num)

print(num_max_sum_div)
