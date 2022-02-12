with open('27-A (4).txt', 'r') as file:
    numbers = file.readlines()

numbers = tuple(map(int, numbers[1:]))
mod_1 = []
mod_2 = []
mod_0 = []
for num in numbers:
    if num % 3 == 0:
        mod_0.append(num)
    elif num % 3 == 2:
        mod_2.append(num)
    elif num % 3 == 1:
        mod_1.append(num)
mod_1.sort()
mod_2.sort()
mod_0.sort()
sum_1 = sum(mod_1[0:3])
sum_0 = sum(mod_0[0:3])
sum_2 = sum(mod_2[0:3])
sum_012 = mod_0[0] + mod_1[0] + mod_2[0]
print(min([sum_1, sum_2, sum_0, sum_012]))
