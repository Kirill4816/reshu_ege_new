with open('17 (10).txt', 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
cnt_pairs = 0
max_sum_pair = 0
average_numbers = 0
cnt_numbers = 0
for number in numbers:
    if number % 2 != 0:
        average_numbers += number
        cnt_numbers += 1

average_numbers = round(average_numbers // cnt_numbers)

for i in range(0, len(numbers) - 1):
    num_1 = numbers[i]
    num_2 = numbers[i + 1]
    if (num_1 % 5 == 0 or num_2 % 5 == 0) and (num_1 < average_numbers or num_2 < average_numbers):
        cnt_pairs += 1
        if num_1 + num_2 > max_sum_pair:
            max_sum_pair = num_1 + num_2
print(cnt_pairs, max_sum_pair)
