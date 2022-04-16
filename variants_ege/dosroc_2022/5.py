for i in range(1, 1001):
    n_2 = bin(i)[2:]
    if i % 2 == 0:
        str = '10' + n_2
    else:
        str = '1' + n_2 + '01'
    n_10 = int(str, 2)
    if n_10 > 516:
        print(i)
