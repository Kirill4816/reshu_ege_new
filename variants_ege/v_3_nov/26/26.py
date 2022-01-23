with open('inf_26_04_21_26.txt', 'r') as file:
    numbers = file.readlines()

numbers = tuple(map(int, numbers[1:]))
print(len(numbers))
first = True
cnt_dif_pair = 0
odd_nums = [num for num in numbers if num % 2 == 0]
even_nums = [num for num in numbers if num % 2 == 1]
for num in odd_nums:
    for enum in even_nums:
        if num + enum in numbers:
            cnt_dif_pair += 1
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if (numbers[i] % 2 != numbers[j] % 2) and numbers[i] + numbers[j] in numbers:
#             cnt_dif_pair += 1
print(cnt_dif_pair)