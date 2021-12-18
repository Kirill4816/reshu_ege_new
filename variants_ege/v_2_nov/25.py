# Найдите все натуральные числа, принадлежащие отрезку [2000000; 3000000],
# у которых составленное описанным способом множество разностей будет содержать не меньше трёх элементов,
# не превышающих 115.
from math import sqrt

first_num = 2000000
second_num = 3000000

for number in range(first_num, second_num + 1):
    cnt_dif = 0
    for divider in range(1000, round(sqrt(number))):
        if number % divider == 0:
            multiplier = number // divider
            if abs(divider - multiplier) <= 115:
                cnt_dif += 1
            if cnt_dif == 3:
                print(number)
                break
