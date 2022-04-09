products = []

with open('26 (9).txt', 'r') as file:
    cnt_products, money = map(int, file.readline().split())
    for i in range(cnt_products):
        price_good, cnt_good, typ = file.readline().split()
        products.append((typ, int(price_good), int(cnt_good)))

products.sort(key=lambda x: (x[0] == 'B', x[1]))

sum_money = 0
cnt_B_goods = 0

for goods in products:
    if sum_money + goods[1] > money:
        break
    for good in range(1, goods[2] + 1):
        if sum_money + goods[1] <= money:
            sum_money += goods[1]
            if goods[0] == 'B':
                cnt_B_goods += 1

print(cnt_B_goods, money - sum_money)
