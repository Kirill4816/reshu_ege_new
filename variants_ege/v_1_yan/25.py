# Найдите все натуральные числа, принадлежащие отрезку [35000000;40000000],
# у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.
from math import sqrt

first_num = 35000000
second_num = 40000000
for number in range(first_num, second_num + 1):
    dividers = []
    for div in range(1, number // 2 + 1):
        if div % 2 != 0:
            if number % div == 0:
                dividers.append(div)
    if len(dividers) == 5:
        print(number)