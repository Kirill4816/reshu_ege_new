# Предприятие производит оптовую закупку некоторых изделий A и B,
# на которую выделена определённая сумма денег.
# У поставщика есть в наличии партии этих изделий различных
# модификаций по различной цене. На выделенные деньги необходимо
# приобрести как можно больше изделий B независимо от модификации.
# Если у поставщика закончатся изделия B,
# то на оставшиеся деньги необходимо приобрести как можно больше изделий A.
# Известны выделенная для закупки сумма,
# а также количество и цена различных модификаций данных изделий у поставщика.
# Необходимо определить, сколько будет закуплено изделий A
# и какая сумма останется неиспользованной.

products = []

with open('26 (5).txt', 'r') as file:
    cnt_products, money = map(int, file.readline().split())
    for i in range(cnt_products):
        price_good, cnt_good, typ = file.readline().split()
        products.append((typ, int(price_good), int(cnt_good)))

products.sort(key=lambda x: (x[0] == 'A', x[1]))

sum_money = 0
cnt_A_goods = 0

for goods in products:
    if sum_money + goods[1] > money:
        break
    for good in range(1, goods[2] + 1):
        if sum_money + goods[1] <= money:
            sum_money += goods[1]
            if goods[0] == 'A':
                cnt_A_goods += 1
print(cnt_A_goods, money - sum_money)
