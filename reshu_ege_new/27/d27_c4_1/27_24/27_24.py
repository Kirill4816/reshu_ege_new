with open('27_24.txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers[1:]))
max_sum_pair = 0
max_num_1 = 0
max_num_2 = 0
for i in range(len(numbers)):
    for g in range(i + 1, len(numbers)):
        num_1 = numbers[i]
        num_2 = numbers[g]
        if (abs(num_1 - num_2) % 2 == 0) and (num_1 % 31 == 0 or num_2 % 31 == 0):
            if num_1 + num_2 > max_sum_pair:
                max_sum_pair = num_1 + num_2
                max_num_1 = num_1
                max_num_2 = num_2

print(max_num_1, max_num_2)
