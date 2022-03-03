with open('27-A (5).txt', 'r') as file:
    numbers = file.read().split()

numbers = numbers[1:]
cnt_nums = 0
sum_nums = 0
max_sum = 0
left_sides = [float('inf') for i in range(30)]
for num in numbers:
    sum_nums += num
    if num % 2 != 0 and num > 0:
        cnt_nums += 1
    div = cnt_nums % 30
    if sum_nums < left_sides[div]:
        left_sides[div] = sum_nums
    if sum_nums - left_sides[div] > max_sum:
        max_sum = sum_nums - left_sides[div]
print(max_sum)
