import os
# Текстовый файл содержит строки различной длины.
# Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.

path = os.path.abspath('16.txt')
with open(path, 'r') as file:
    strings = file.readlines()

cnt_str = 0
cnt_A = 0
cnt_E = 0
for string in strings:
    for symbol in string:
        if symbol == 'A':
            cnt_A += 1
        if symbol == 'E':
            cnt_E += 1
    if cnt_E > cnt_A:
        cnt_str += 1
    cnt_A = 0
    cnt_E = 0
print(cnt_str)
