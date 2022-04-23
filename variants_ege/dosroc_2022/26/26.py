numbers = []

with open('26 (11).txt', 'r') as file:
    cnt = map(int, file.readline().split())
    for i in range(cnt):
        num_row, num_place = file.readline().split()
        numbers.append((int(num_row), int(num_place)))
print(numbers)
# numbers.sort(key=lambda  x: ())
