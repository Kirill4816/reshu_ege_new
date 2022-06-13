with open('27-B_demo.txt', 'r') as file:
    numbers = file.readlines()

first = True
max_sum_3 = 0
min_dif = 10000

for num in numbers:
    if first:
        first = False
        continue
    num = tuple(map(int, num.split()))
    if num[0] > num[1]:
        max_sum_3 += num[0]
    else:
        max_sum_3 += num[1]
    dif = abs(num[0] - num[1])
    if dif % 3 != 0 and dif < min_dif:
        min_dif = dif

if max_sum_3 % 3 != 0:
    print(max_sum_3)
else:
    print(max_sum_3 - min_dif)
