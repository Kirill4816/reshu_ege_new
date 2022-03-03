with open('27_3.txt', 'r', encoding='UTF-8') as file:
    numbers = file.readlines()

max_y_pos = 1
min_y_pos = float('inf')
max_x_pos = 1
max_y_neg = -1 * float('inf')
min_y_neg = -1
max_x_neg = -1

for string in numbers[1:]:
    x, y = tuple(map(int, string.split()))
    if x == 0 and y > 0:
        if y > max_y_pos:
            max_y_pos = y
        if y < min_y_pos:
            min_y_pos = y
    if x == 0 and y < 0:
        if y > max_y_neg:
            max_y_neg = y
        if y < min_y_neg:
            min_y_neg = y
    if y > 0:
        if abs(x) > max_x_pos:
            max_x_pos = abs(x)
    if y < 0:
        if abs(x) > max_x_neg:
            max_x_neg = abs(x)
print(min_y_neg, min_y_pos, max_x_neg, max_y_neg, max_x_pos, max_y_pos)

if min_y_pos != float('inf'):
    s_pos = abs(max_y_pos - min_y_pos) * max_x_pos / 2
else:
    s_pos = 0
if min_y_neg != -1 * float('inf'):
    s_neg = abs(max_y_neg - min_y_neg) * max_x_neg / 2
else:
    s_neg = 0

if s_pos == 0 and s_neg == 0:
    print('треуголника не существует')
else:
    print(max([s_neg, s_pos]))
