with open('17 (8).txt', 'r') as file:
    numbers = file.read()

numbers = list(map(int, numbers.split()))
cnt_pair = 0
max_pair = 0
for i in range(1, len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        cnt_pair += 1
        if (a + b) > max_pair:
            max_pair = a + b
print(cnt_pair, max_pair)
