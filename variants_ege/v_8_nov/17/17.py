# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 80,
# затем максимальную из разностей элементов таких пар.
with open('17 (6).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
len_nums = len(numbers)
cnt_80 = 0
max_80 = 0

for i in range(len_nums):
    for g in range(i + 1, len_nums):
        if i != g:
            diff = abs(numbers[i] - numbers[g])
            if diff % 80 == 0:
                cnt_80 += 1
                if diff > max_80:
                    max_80 = diff
print(cnt_80, max_80)
a = [1, 7, 5, 1, 3]
b = [1, 7, 5, 1, 3]
