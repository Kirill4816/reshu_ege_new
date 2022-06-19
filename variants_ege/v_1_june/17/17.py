with open("17 (20).txt", 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
cnt_pairs = 0
sum_even = 0
average_nums = 0
cnt_even = 0
max_sum = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
        cnt_even += 1

average_nums = sum_even // cnt_even

for i in range(1, len(numbers) - 1):
    if (numbers[i] % 3 == 0 and numbers[i + 1] % 3 != 0) or (numbers[i] % 3 != 0 and numbers[i + 1] % 3 == 0) or \
            (numbers[i] % 3 == 0 and numbers[i + 1] % 3 == 0):
        if numbers[i] < average_nums or numbers[i + 1] < average_nums:
            cnt_pairs += 1
            if numbers[i] + numbers[i + 1] > max_sum:
                max_sum = numbers[i] + numbers[i + 1]

print(cnt_pairs, max_sum)
