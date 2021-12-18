# Пусть M(N)— произведение 5 наименьших различных натуральных делителей натурального числа N,
# не считая единицы. Если у числа N меньше 5 таких делителей,
# то M(N) считается равным нулю.
#
# Найдите 5 наименьших натуральных чисел, превышающих 500000000,
# для которых 0 < M(N)< N.
# В ответе запишите найденные значения M(N)
# в порядке возрастания соответствующих им чисел N.

from math import sqrt


for num in range(500000001, 500000100):
    dividers = []
    for div in range(2, round(sqrt(num))):
        if num % div == 0:
            dividers.append(div)
    if len(dividers) > 5:
        dividers = sorted(dividers)[:5]
        M = 1
        for numbers in dividers:
            M *= numbers
        if M < num:
            print(M)
