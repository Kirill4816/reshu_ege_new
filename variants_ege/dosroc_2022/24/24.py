# Текстовый файл состоит не более, чем из 10^6 символов из набора A, B, C.
# Найдите максимальное количество подряд идущих пар символов АС или АВ.
# Искомая подстрока может включать только пары АВ,
# только пары АС или содержать одновременно как пары АС, так и пары АВ
with open('24 (8).txt', 'r') as file:
    f = file.read()
string = f.replace('AC', 'AB')


max_len = 0
cur_len = 0
previous = 'B'
dict_ab = {
    'A': 'B',
    'B': 'A'
}
for symbol in string:
    if symbol == dict_ab[previous]:
        cur_len += 1
        previous = symbol
    else:
        previous = 'B'
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 0

if cur_len > max_len:
    max_len = cur_len

print(max_len)


# for i in range(1, 100000):
#     ab = 'AB' * i
#     if ab in strings:
#         print(i)

