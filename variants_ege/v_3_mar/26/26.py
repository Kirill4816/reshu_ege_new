with open('inf_22_10_20_26 (2).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers[1:]))

nums_less_100 = []
nums_more_100 = []

for num in numbers:
    if num <= 100:
        nums_less_100.append(num)
    else:
        nums_more_100.append(num)

nums_more_100.sort()

len_nums_more_100 = len(nums_more_100)
nums_for_sale = nums_more_100[:len_nums_more_100 // 2]
big_nums_without_sale = nums_more_100[len_nums_more_100 // 2:]

del nums_more_100

max_sale_num = nums_for_sale[-1]
nums_for_sale = list(map(lambda x: x * .7, nums_for_sale))
sum_nums_for_sale = sum(nums_for_sale)
sum_nums_for_sale = int(sum_nums_for_sale) if sum_nums_for_sale == int(sum_nums_for_sale) else int(sum_nums_for_sale) + 1

result = sum(nums_less_100 + big_nums_without_sale + [sum_nums_for_sale])
print(result, max_sale_num)