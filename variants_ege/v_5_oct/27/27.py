with open('27_B.txt', 'r') as file:
    numbers = file.readlines()

first = True
min_sum_3 = 0
min_dif = 10000
for num in numbers:
    if first:
        first = False
        continue
    num = num.split()
    num = tuple(map(int, num))
    if num[0] > num[1]:
        min_sum_3 += num[1]
    else:
        min_sum_3 += num[0]
    dif = abs(num[0] - num[1])
    if dif % 3 != 0 and dif < min_dif:
        min_dif = dif
if min_sum_3 % 3 != 0:
    print(min_sum_3)
else:
    print(min_sum_3 + min_dif)
