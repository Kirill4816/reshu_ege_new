# Найдите все натуральные числа N, принадлежащие отрезку [200000000;400000000],
# которые можно представить в виде N=2^m·3^n, где m — чётное число,
# n — нечётное число.
# В ответе запишите все найденные числа в порядке возрастания.

for m in range(2, 1000, 2):
    for n in range(1, 1001, 2):
        N = 2 ** m * 3 ** n
        if 200000000 < N < 400000000:
            print(N)
