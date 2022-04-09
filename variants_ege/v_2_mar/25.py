from math import sqrt

first_num = 289123456
second_num = 389123456
more_divider = 0

for number in range(first_num, second_num + 1):
    if sqrt(number) == int(sqrt(number)):
        cnt_div = 0
        more_divider = 0
        for divider in range(2, round(sqrt(number)) + 1):
            if number % divider == 0:
                if divider ** 2 == number:
                    cnt_div += 1
                    if more_divider < divider:
                        more_divider = divider
                else:
                    cnt_div += 2
                    div_2 = number / divider
                    if divider > div_2:
                        if more_divider < divider:
                            more_divider = divider
                    else:
                        if more_divider < div_2:
                            more_divider = div_2
        if cnt_div == 3:
            print(f'{number}\t\t{int(more_divider)}')
