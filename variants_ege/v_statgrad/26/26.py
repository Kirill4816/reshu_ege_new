with open('26.txt', 'r') as file:
    numbers = file.readlines()

numbers = numbers[1:]
field = dict()

for row in numbers:
    x, y = tuple(map(int, row.split()))
    if y % 2 != 0:
        continue
    if x in field:
        field[x].add(y)
    else:
        field[x] = {y}

max_cnt = 0
max_row = 0
for x, y in field.items():
    cnt = len(y)
    if cnt > max_cnt:
        max_cnt = cnt
        max_row = x
    elif cnt == max_cnt and x > max_row:
        max_row = x

print(max_cnt, max_row)
