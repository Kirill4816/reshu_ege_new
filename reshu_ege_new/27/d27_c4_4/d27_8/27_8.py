from math import sqrt
with open('27_8.txt', 'r') as file:
    strings = file.readlines()

max_point_1 = 0
max_point_4 = 0
for string in strings[1:]:
    x, y = tuple(map(int, string.split()))
    if x == y:
        distance_1 = sqrt(x ** 2 + y ** 2)
        if max_point_1 < distance_1:
            max_point_1 = distance_1
    if x == -1 * y:
        distance_4 = sqrt(x ** 2 + y ** 2)
        if max_point_4 < distance_4:
            max_point_4 = distance_4

print(distance_1 * distance_4 / 2)
