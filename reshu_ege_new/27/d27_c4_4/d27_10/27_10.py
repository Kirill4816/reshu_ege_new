with open('27_10.txt', 'r') as file:
    strings = file.readlines()

cnt = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for string in strings[1:]:
    x, y = tuple(map(int, string.split()))
    if x == 0 or y == 0:
        continue
    if x > 0 and y > 0:
        cnt_1 += 1
    elif x < 0 and y > 0:
        cnt_2 += 1
    elif x < 0 and y < 0:
        cnt_3 += 1
    elif x > 0 and y < 0:
        cnt_4 += 1

cnt = cnt_1 * cnt_2 + cnt_1 * cnt_4 + cnt_2 * cnt_3 + cnt_3 * cnt_4

print(cnt)
