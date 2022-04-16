for x in range(1, 1000):
    s = x
    P = 10
    Q = 8
    K1 = 0
    K2 = 0
    while s <= 100:
        s = s + P
        K1 = K1 + 1
    while s >= Q:
        s = s - Q
        K2 = K2 + 1
    K1 += s
    K2 += s

    if K1 == 10 and K2 == 19:
        print(x)
        break
