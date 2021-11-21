# Текстовый файл состоит не более чем из 106 символов A, B и C.
# Определите максимальную длину цепочки вида ABABAB...
# (составленной из фрагментов AB, последний фрагмент может быть неполным).

import os
path = os.path.abspath('zadanie24_1.txt')

with open(path, 'r') as file:
    f = file.read()

max_seq_len = 0
cur_seq_len = 0
previous = 'B'
next_dict = {
    'A': 'B',
    'B': 'A'
}
for symbol in f:
    if symbol == next_dict[previous]:
        cur_seq_len += 1
        previous = symbol
    else:
        previous = 'B'
        if cur_seq_len > max_seq_len:
            max_seq_len = cur_seq_len
        cur_seq_len = 0

if cur_seq_len > max_seq_len:
    max_seq_len = cur_seq_len

print(max_seq_len)
