# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите длину самой длинной последовательности,
# состоящей из символов X.
# Хотя бы один символ X находится в последовательности.

import os

path = os.path.abspath('24.txt')

with open(path, 'r') as file:
    f = file.read()

max_seq_len = 0
cur_seq_len = 0
for symbol in f:
    if symbol == 'X':
        cur_seq_len += 1
    elif cur_seq_len:
        if cur_seq_len > max_seq_len:
            max_seq_len = cur_seq_len
        cur_seq_len = 0
if cur_seq_len > max_seq_len:
    max_seq_len = cur_seq_len

print(max_seq_len)
