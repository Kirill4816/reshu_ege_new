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
    if sqrt(number) == int(sqrt(number)):
        cnt_div = 0
        for divider in range(2, round(sqrt(number))):
            if number % divider == 0:
                if divider ** 2 == number:
                    cnt_div += 1
                    more_divider = divider
                else:
                    cnt_div += 2
                    if divider > number / divider:
                        more_divider = divider
                    else:
                        more_divider = number / divider
            # if cnt_div > 5:
            #     break
        if cnt_div == 5:
            print(f'{number}\t\t{more_divider}')
