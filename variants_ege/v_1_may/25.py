from math import sqrt

first_num = 35000000
second_num = 40000000
for number in range(first_num, second_num + 1):
    dividers = []
    for div in range(1, round(sqrt(number))):
        if number % div == 0:
            if div % 2:
                dividers.append(div)
            div_2 = number // div
            if div_2 % 2 and div != div_2:
                dividers.append(div_2)
    if len(dividers) == 5:
        print(number)
