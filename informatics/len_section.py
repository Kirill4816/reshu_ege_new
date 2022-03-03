from math import sqrt

def distance(x1, x2, y1, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


x1 = float(input())
y1 = float(input())
y2 = float(input())
x2 = float(input())

print(distance(x1, x2, y1, y2))
