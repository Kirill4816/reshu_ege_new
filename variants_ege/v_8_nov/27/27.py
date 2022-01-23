# Дана последовательность из N натуральных чисел.
# Рассматриваются все её непрерывные подпоследовательности,
# такие что сумма элементов каждой из них кратна k=43.
# Найдите среди них подпоследовательность с максимальной суммой,
# определите её длину. Если таких подпоследовательностей найдено несколько,
# в ответе укажите количество элементов самой короткой из них.

with open('27_A.txt', 'r') as file:
    first = True
    mod_43 = [100000000000000000000000001 for i in range(43)]
    max_len_43 = [0 for i in range(43)]
    summ = 0
    max_summ = 0
    min_len = 10000
    cnt_numbers = 0
    for line in file.readlines():
        if first:
            first = False
            continue
        cnt_numbers += 1
        line = int(line)
        summ += line
        div = summ % 43
        if div == 0:
            max_summ = summ
            min_len = cnt_numbers
        else:
            dif = summ - mod_43[div]
            l = cnt_numbers - max_len_43[div]
            if dif > max_summ:
                max_summ = dif
                min_len = l
            if dif == max_summ and l < min_len:
                min_len = l
        if summ < mod_43[div]:
            mod_43[div] = summ
            max_len_43[div] = cnt_numbers
print(min_len)

