import os
# Текстовый файл содержит строки различной длины.
# Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква A встречается чаще, чем буква E.

path = os.path.abspath('17.txt')

with open(path, 'r') as file:
    strings = file.readlines()

cnt = 0
for string in strings:
    if string.count('A') > string.count('E'):
        cnt += 1
print(cnt)
