with open('27_2.txt', 'r') as file:
    numbers = file.readlines()

min_x = float('inf')
min_y = float('inf')

for string in numbers[1:]:
    x, y = tuple(map(int, string.split()))
    if (x != 0 and y != 0) or (x == 0 and y == 0):
        continue
    else:
        if x == 0:
            if abs(y) < min_y:
                min_y = abs(y)
        else:
            if abs(x) < min_x:
                min_x = abs(x)

if min_x == float('inf') or min_y == float('inf'):
    print('треугольник не существует')
else:
    print(min_y * min_x / 2)
