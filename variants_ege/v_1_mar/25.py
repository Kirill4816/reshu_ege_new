from math import sqrt

first_num = 123456789
second_num = 223456789
more_divider = 0

for number in range(first_num, second_num + 1):
    if sqrt(number) == int(sqrt(number)):
        cnt_div = 0
        for divider in range(2, round(sqrt(number))):
            if number % divider == 0:
                if divider ** 2 == number:
                    cnt_div += 1
                    more_divider = divider
                else:
                    cnt_div += 2
                    if divider > number / divider:
                        more_divider = divider
                    else:
                        more_divider = number / divider
        if cnt_div == 5:
            print(f'{number}\t\t{more_divider}')
