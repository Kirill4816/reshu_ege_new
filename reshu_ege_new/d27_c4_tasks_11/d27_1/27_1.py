with open('27_1.txt', 'r') as file:
    numbers = file.readlines()

max_x = 0
max_y = 0

for string in numbers[1:]:
    x, y = tuple(map(int, string.split()))
    if (x != 0 and y != 0) or (x == 0 and y == 0):
        continue
    else:
        if x == 0:
            if abs(y) > max_y:
                max_y = abs(y)
        else:
            if abs(x) > max_x:
                max_x = abs(x)

if max_x == 0 or max_y == 0:
    print('треугольник не существует')
else:
    print(max_y * max_x / 2)
