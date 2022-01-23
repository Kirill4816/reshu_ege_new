with open('17 (7).txt', 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
cnt = 0
max_sum = 0
for i in range(0, len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]
    max_num = max([a, b, c])
    min_num = min([a, b, c])
    mid_num = sum([a, b, c]) - min_num - max_num
    if max_num ** 2 < mid_num ** 2 + min_num ** 2:
        cnt += 1
        if sum([a, b, c]) > max_sum:
            max_sum = sum([a, b, c])
print(cnt, max_sum)
