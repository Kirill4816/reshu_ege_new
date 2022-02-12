def IsPointInSquare(x, y):
    first = ((x > 0 and y > 0) and (y <= 1 - x))
    second = ((x > 0 and y < 0) and (y >= x - 1))
    third = ((x < 0 and y > 0) and (y <= 1 + x))
    fourth = ((x < 0 and y < 0) and (y >= -1 + x))
    fifth = ((x == 0 and -1 <= y <= 1) or (y == 0 and -1 <= x <= 1))
    return first or second or third or fourth or fifth


x = float(input())
y = float(input())
print(IsPointInSquare(x, y))
