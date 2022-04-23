# numbers = []
numbers = {}
max_row = 0
with open('26 (11).txt', 'r') as file:
    cnt = int(file.readline().strip())
    for i in range(cnt):
        num_row, num_place = tuple(map(int, file.readline().split()))
        # numbers.append((int(num_row), int(num_place)))
        if num_row > max_row:
            max_row = num_row
        if num_row not in numbers:
            numbers[num_row] = [num_place]
        else:
            numbers[num_row].append(num_place)


for num_row in range(max_row, 0, -1):
    if num_row not in numbers:
       continue
    row = numbers[num_row]
    row.sort()
    for i in range(len(row) - 1):
        dif = row[i + 1] - row[i]
        if dif == 12:
            print(num_row, row[i])
            break

# print(numbers)
# numbers.sort(key=lambda  x: ())
