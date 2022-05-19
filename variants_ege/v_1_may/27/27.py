with open('27-B (7).txt', 'r') as file:
    numbers = file.readlines()

numbers = tuple(map(int, numbers[1:]))
num_3_1 = []
num_3_2 = []
num_3_0 = []

for num in numbers:
    if num % 3 == 0:
        num_3_0.append(num)
    elif num % 3 == 2:
        num_3_2.append(num)
    elif num % 3 == 1:
        num_3_1.append(num)

num_3_1.sort(reverse=True)
num_3_2.sort(reverse=True)
num_3_0.sort(reverse=True)

sum_1 = (num_3_1[0] + num_3_1[1] + num_3_1[2])
sum_0 = (num_3_0[0] + num_3_0[1] + num_3_0[2])
sum_2 = (num_3_2[0] + num_3_2[1] + num_3_2[2])

sum_012 = num_3_0[0] + num_3_1[0] + num_3_2[0]
print(max([sum_1, sum_2, sum_0, sum_012]))
