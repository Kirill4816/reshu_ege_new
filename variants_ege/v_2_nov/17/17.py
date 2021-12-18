with open('17 (3).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
num_5_chet = 0
num_5_nechet = 0
num_chet = 0
num_nechet = 0
max_5_chet = 0
max_5_nechet = 0
max_chet = 0
max_nechet = 0
for num in numbers:
    if num % 2 == 0:
        num_chet += 1
        if num > max_chet:
            max_chet = num
        if num % 5 == 0:
            num_5_chet += 1
            if num > max_5_chet:
                max_5_chet = num
    else:
        num_nechet += 1
        if num > max_nechet:
            max_nechet = num
        if num % 5 == 0:
            num_5_nechet += 1
            if num > max_5_nechet:
                max_5_nechet = num

cnt = num_5_chet * num_nechet + num_5_nechet * num_chet - num_5_chet * num_5_nechet
max_sum = max((max_chet + max_5_nechet, max_nechet + max_5_chet))
print(cnt, max_sum)
