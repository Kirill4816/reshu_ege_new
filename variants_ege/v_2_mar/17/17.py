with open('17 (14).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
cnt_odd = 0
cnt_even = 0
cnt_31_odd = 0
cnt_31_even = 0
max_num_odd = 0
max_num_even = 0
max_num_31_odd = 0
max_num_31_even = 0
for num in numbers:
    is_used = False
    if num % 2 == 0:
        if num % 31 == 0:
            cnt_31_odd += 1
            if num > max_num_31_odd:
                if max_num_odd < max_num_31_odd:
                    max_num_odd = max_num_31_odd
                max_num_31_odd = num
                is_used = True
        else:
            cnt_odd += 1
        if not is_used and num > max_num_odd:
            max_num_odd = num
    else:
        if num % 31 == 0:
            cnt_31_even += 1
            if num > max_num_31_even:
                if max_num_even < max_num_31_even:
                    max_num_even = max_num_31_even
                max_num_even = num
                is_used = True
        else:
            cnt_even += 1
        if not is_used and num > max_num_even:
            max_num_even = num

cnt = 