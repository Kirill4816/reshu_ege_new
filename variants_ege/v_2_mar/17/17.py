with open('17 (14).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))
cnt = 0
max_sum = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        num_1 = numbers[i]
        num_2 = numbers[j]
        if abs(num_2 - num_1) % 2 == 0 and (num_2 % 31 == 0 or num_1 % 31 == 0):
            cur_sum = num_2 + num_1
            cnt += 1
            if cur_sum > max_sum:
                max_sum = cur_sum

print(cnt, max_sum)

# cnt_odd = 0
# cnt_even = 0
# cnt_31_odd = 0
# cnt_31_even = 0
# max_num_odd = 0
# max_num_even = 0
# max_num_31_odd = 0
# max_num_31_even = 0
# for num in numbers:
#     is_used = False
#     if num % 2 == 0:
#         if num % 31 == 0:
#             cnt_31_odd += 1
#             if num > max_num_31_odd:
#                 if max_num_odd < max_num_31_odd:
#                     max_num_odd = max_num_31_odd
#                 max_num_31_odd = num
#                 is_used = True
#         else:
#             cnt_odd += 1
#         if not is_used and num > max_num_odd:
#             max_num_odd = num
#     else:
#         if num % 31 == 0:
#             cnt_31_even += 1
#             if num > max_num_31_even:
#                 if max_num_even < max_num_31_even:
#                     max_num_even = max_num_31_even
#                 max_num_even = num
#                 is_used = True
#         else:
#             cnt_even += 1
#         if not is_used and num > max_num_even:
#             max_num_even = num
#
# cnt = cnt_odd * cnt_31_odd + cnt_even * cnt_31_even
#
# for i in range(1, cnt_31_odd):
#     cnt += i
#
# for j in range(1, cnt_31_even):
#     cnt += j
#
# sum_1 = max_num_odd + max_num_31_odd
# sum_2 = max_num_even + max_num_31_even
#
# print(cnt, max((sum_1, sum_2)))
