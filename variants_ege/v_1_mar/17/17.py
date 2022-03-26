import os

path = os.path.abspath("17 (13).txt")

with open(path, 'r') as file:
    numbers = file.read()
    numbers = numbers.split()
    numbers = list(map(int, numbers))

mod_160_num_7 = []
mod_cnt = [0] * 160
max_not_7 = 0
max_7 = 0
prev_max_7 = 0
for number in numbers:
    mod_160 = number % 160
    if number % 7 == 0:
        mod_160_num_7.append(mod_160)
        if number > max_7:
            prev_max_7 = max_7
            max_7 = number
        elif number > prev_max_7:
            prev_max_7 = number
    else:
        mod_cnt[mod_160] += 1
        if number > max_not_7:
            max_not_7 = number
pairs_cnt = 0
s = sum(mod_cnt)
for i in mod_160_num_7:
    pairs_cnt += s - mod_cnt[i]

l = len(mod_160_num_7)
for i in range(l):
    for j in range(i + 1, l):
        if mod_160_num_7[i] != mod_160_num_7[j]:
            pairs_cnt += 1

if max_not_7 > prev_max_7:
    max_sum = max_7 + max_not_7
else:
    max_sum = max_7 + prev_max_7

print(pairs_cnt, max_sum)
