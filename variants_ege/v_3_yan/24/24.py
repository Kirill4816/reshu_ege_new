# Текстовый файл состоит не более чем из 10^6 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.

with open('24_demo.txt', 'r') as file:
    strings = file.readlines()

max_cnt_rep_symbols = 1
cnt_rep_symbols = 1

for string in strings:
    for i in range(len(string)):
        if string[i] != string[i - 1]:
            cnt_rep_symbols += 1
        else:
            if cnt_rep_symbols > max_cnt_rep_symbols:
                max_cnt_rep_symbols = cnt_rep_symbols
            cnt_rep_symbols = 1

print(max_cnt_rep_symbols)
