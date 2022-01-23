with open('inf_26 (1).txt', 'r') as file:
    lines = file.readlines()


prices_not_sale = []
prices_sale = []
sum_prices = 0
numbers_more_100 = []
numbers_less_100 = []
lines = list(map(int, lines))
lines.remove(lines[0])
for num in lines:
    if num > 100:
        numbers_more_100.append(num)
    else:
        numbers_less_100.append(num)
numbers_more_100.sort()
half = len(numbers_more_100) // 2
prices_sale = numbers_more_100[:half]
for num in prices_sale:
    sum_prices += num - (num * 0.3)
prices_not_sale = numbers_more_100[half:]
for num in prices_not_sale:
    sum_prices += num
for num in numbers_less_100:
    sum_prices += num
if int(sum_prices) != sum_prices:
    sum_prices = int(sum_prices) + 1
print(sum_prices, prices_sale[-1])
