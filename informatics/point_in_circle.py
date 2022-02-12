from math import sqrt


def IsPointInCircle(x, y, xc, yc, r):
    lenn = distance(x, y, xc, yc)
    return lenn <= r


def distance(x, y, xc, yc):
    return sqrt((x - xc) ** 2 + (y - yc) ** 2)


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
print(IsPointInCircle(x, y, xc, yc, r))
