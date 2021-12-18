with open('17 (5).txt', 'r') as file:
    numbers = file.read().split()

numbers = map(int, numbers)
div_cnt = [0, 0, 0, 0, 0]
div_max = [0, 0, 0, 0, 0]
prev_max = 0
for num in numbers:
    mod = num % 5
    div_cnt[mod] += 1
    if mod == 0:
        if num > div_max[0]:
            prev_max = div_max[0]
            div_max[0] = num
        elif num > prev_max:
            prev_max = num
    elif num > div_max[mod]:
        div_max[mod] = num
