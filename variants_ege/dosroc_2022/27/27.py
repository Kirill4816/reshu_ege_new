with open('27-B (6).txt', 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers[1:]))
l = len(numbers)
numbers_1 = numbers * 2
sum_1 = 0
for i in range(l // 2 + 1):
    sum_1 += numbers[i] * i
k = l // 2 - 1
for j in range(i + 1, l):
    sum_1 += numbers[j] * k
    k -= 1
res = [sum_1]

for i in range(l * 2 - 1):
    numbers_1[i + 1] += numbers_1[i]

for i in range(l):
    res.append(res[i] + (numbers_1[l + i] - numbers_1[i + l // 2]) - (numbers_1[i + l // 2] - numbers_1[i]))

print(res.index(min(res)) + 1)
