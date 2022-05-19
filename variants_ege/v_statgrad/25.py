from math import sqrt
numbers = []

for i in range(7000000, 7000100):
    if len(numbers) == 5:
        break
    dividers = 0
    for div in range(2, round(sqrt(i)) + 1):
        if dividers > 2:
            break
        elif i % div == 0:
            dividers += 1
    else:
        numbers.append(i - 7000000)

print(numbers)
