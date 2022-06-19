with open("17 (18).txt", 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
cnt_pairs = 0
min_num = float('inf')
dif_pairs = []

for num in numbers:
    if num % 2 != 0:
        if num < min_num:
            min_num = num

for i in range(1, len(numbers) - 1):
    if (numbers[i] % 3 == 0 and numbers[i + 1] % 3 != 0) or (numbers[i] % 3 != 0 and numbers[i + 1] % 3 == 0):
        cnt_pairs += 1
        pair_dif = abs(numbers[i] - numbers[i + 1])
        if pair_dif < min_num:
            dif_pairs.append(pair_dif)

dif_pairs.sort(reverse=True)

print(cnt_pairs, dif_pairs[0])
