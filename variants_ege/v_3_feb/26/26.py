with open('26 (7).txt', 'r') as file:
    numbers = file.readlines()

# numbers = numbers[1:]
# max_pair = 0
# time = 1633305600
# for index, num in enumerate(numbers):
#     pair_1, pair_2 = map(int, num.split())
#     numbers[index] = (pair_1, pair_2)
#     if max([pair_1, pair_2]) > max_pair:
#         max_pair = max([pair_1, pair_2])
# cnts = []
# print(1)
# for t in range(time, max_pair + 1):
#     cnt_process = 0
#     for pair in numbers:
#         if pair[0] <= t <= pair[1] or (pair[0] <= t and pair[1] == 0):
#             cnt_process += 1
#     cnts.append(cnt_process)
#     print(t)
# max_num = max(cnts)
# print(max_num, cnts.count(max_num))

numbers = numbers[1:]
start_time