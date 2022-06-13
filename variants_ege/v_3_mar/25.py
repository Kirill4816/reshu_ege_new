import math

first_num = 200000000
second_num = 400000000

#numbers = tuple(range(first_num, second_num + 1))

max_m = int(math.log2(second_num / 3))
max_n = int(math.log(second_num, 3))

#print(max_n, max_m)

nums = []

for m in range(0, max_m + 1, 2):
    for n in range(1, max_n + 1, 2):
        num = (2 ** m) * (3 ** n)
        if first_num <= num <= second_num:
            nums.append(num)

nums.sort()
print(*nums, sep="\n")