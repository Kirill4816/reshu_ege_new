with open('27_5.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers[1:]))
cnt = 0
mods = [0] * 7
for number in numbers:
    mods[number % 7] += 1

cnt = mods[1] * mods[6] + mods[2] * mods[5] + mods[3] * mods[4] + (((mods[0] - 1) + 1) / 2) * (mods[0] - 1)

print(cnt)
