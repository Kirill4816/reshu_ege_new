for i in range(10):
    for g in range(10):
        number = int('12345' + str(i) + '6' + str(g) + '8')
        if number % 17 == 0:
            div_num = number // 17
            print(number, div_num)
