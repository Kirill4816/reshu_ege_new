with open('26 (6).txt', 'r') as file:
    f = file.read().split()

numbers = list(map(int, f))
total_weight = numbers[0]
weights = numbers[2:]
weights.sort()

cnt_containers = 0
max_weight = 0
previous_weight = 0

for num in weights:
    if total_weight - num >= 0:
        cnt_containers += 1
        total_weight -= num
        previous_weight = num
    else:
        total_weight += previous_weight
        break

weights.sort(reverse=True)
for num in weights:
    if total_weight - num >= 0:
        max_weight = num
        break

print(cnt_containers, max_weight)
