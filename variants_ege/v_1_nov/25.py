# Назовём нетривиальным делителем натурального числа его делитель,
# не равный единице и самому числу. Например, у числа 6 есть два нетривиальных делителя: 2 и 3.
# Найдите все натуральные числа, принадлежащие отрезку [289123456;389123456] и имеющие ровно три нетривиальных делителя.
# Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель.
# Ответы расположите в порядке возрастания.
from math import sqrt

first_num = 289123456
second_num = 389123456
more_divider = 0

for number in range(first_num, second_num + 1):
    for divider in range(2, round(sqrt(number))):
        cnt_div = 0
        if number % divider == 0:
            cnt_div += 1
            more_divider = divider
    if cnt_div == 3:
        print(f'{number}\t\t{more_divider}')
