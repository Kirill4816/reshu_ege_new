a = []
N = 2019
min_even = 20000
max_even = 0
for number in a:
    if number % 2 == 0:
        if number > max_even:
            max_even = number
        if number < min_even:
            min_even = number

if min_even == 20000:
    min_even = 0

average_min_max = min_even + max_even // 2

for i in range(0, N):
    num = a[i]
    if num % 2 != 0:
        if num > average_min_max:
            num -= average_min_max

print(a)
