with open('d27_6.txt', 'r') as file:
    numbers = file.readlines()

max_x_Ox_1 = 0
min_x_Ox_2 = float('inf')
max_pos_y = 0
max_neg_y = 0

for string in numbers[1:]:
    x, y = tuple(map(int, string.split()))
    if y == 0 and x > max_x_Ox_1:
        max_x_Ox_1 = x
    if y == 0 and x < min_x_Ox_2:
        min_x_Ox_2 = x
    if y > max_pos_y:
        max_pos_y = y
    if y < max_neg_y:
        max_neg_y = y

base = abs(max_x_Ox_1 - min_x_Ox_2)
s_1 = base * max_pos_y / 2
s_2 = base * abs(max_neg_y) / 2
print(s_1 + s_2)
