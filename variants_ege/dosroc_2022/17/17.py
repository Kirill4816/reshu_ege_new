with open('17 (15).txt', 'r') as file:
    nums = file.read()

min_num_17 = 10001
cnt_pairs = 0
max_sum_pair = 0
numbers = tuple(map(int, nums.split()))

for number in numbers:
    if number % 17 == 0:
        if number < min_num_17:
            min_num_17 = number
print(min_num_17)

for i in range(1, len(numbers)):
    g = i - 1
    if numbers[i] % min_num_17 == 0 or numbers[g] % min_num_17 == 0:
        cnt_pairs += 1
        if numbers[i] + numbers[g] > max_sum_pair:
            max_sum_pair = numbers[i] + numbers[g]

print(cnt_pairs, max_sum_pair)
