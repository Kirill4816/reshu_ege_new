with open('17.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

min_number = 11000
cnt_pairs = 0
max_dif_nums = 0

for number in numbers:
    if number % 2 != 0:
        if number < min_number:
            min_number = number

print(min_number)

for i in range(len(numbers) - 1):
    if (numbers[i] % 3 == 0 and numbers[i + 1] % 3 != 0) or (numbers[i] % 3 != 0 and numbers[i + 1] % 3 == 0):
        if abs(numbers[i] - numbers[i + 1]) < min_number:
            cnt_pairs += 1
            if abs(numbers[i] - numbers[i + 1]) > max_dif_nums:
                max_dif_nums = abs(numbers[i] - numbers[i + 1])

print(cnt_pairs, max_dif_nums)
