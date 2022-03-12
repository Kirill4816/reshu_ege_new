with open('27_9.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
mods = [0] * 117
max_sum = 0
num_0 = 0
num_1 = 0
num_2 = 0

for number in numbers[1:]:
    div = number % 117
    if div != 0:
        if mods[div] < number:
            mods[div] = number
    else:
        if number > mods[0]:
            num_0 = mods[0]
            mods[0] = number
        elif number > num_0:
            num_0 = number

for i in range(1, 117 // 2 + 1):
    if mods[i] != 0 and mods[117 - i] != 0:
        s = mods[i] + mods[117 - i]
        if s > max_sum:
            max_sum = s
            num_1 = mods[i]
            num_2 = mods[117 - i]

s = mods[0] + num_0
if s > max_sum:
    max_sum = s
    num_1 = mods[0]
    num_2 = num_0

print(num_1, num_2)
