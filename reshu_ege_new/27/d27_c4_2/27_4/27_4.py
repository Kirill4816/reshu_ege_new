with open('27_4.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers[1:]))
max_odd_5 = 0
max_odd_n_5 = 0
max_even_5 = 0
max_even_n_5 = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0


for number in numbers:
    if number % 2 == 0:
        if number % 5 == 0:
            if number > max_even_5:
                max_even_5 = number
        else:
            if number > max_even_n_5:
                max_even_n_5 = number
    else:
        if number % 5 == 0:
            if number > max_odd_5:
                max_odd_5 = number
        else:
            if number > max_odd_n_5:
                max_odd_n_5 = number

if max_odd_5 == 0 or max_even_n_5 == 0:
    sum_1 = 0
else:
    sum_1 = max_odd_5 + max_even_n_5
if max_even_5 == 0 or max_odd_n_5 == 0:
    sum_2 = 0
else:
    sum_2 = max_even_5 + max_odd_n_5
if max_even_5 == 0 or max_odd_5 == 0:
    sum_3 = 0
else:
    sum_3 = max_even_5 + max_odd_5

max_pair = max([sum_1, sum_2, sum_3])

if max_pair != 0:
    if max_pair == sum_1:
        print(max_odd_5, max_even_n_5)
    elif max_pair == sum_2:
        print(max_even_5, max_odd_n_5)
    elif max_pair == sum_3:
        print(max_even_5, max_odd_5)
else:
    print(0)
