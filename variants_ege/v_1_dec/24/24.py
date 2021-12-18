# Текстовый файл состоит не более,
# чем из 10^7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки,
# в которой символы «a» и «d» не стоят рядом.

with open('24 (3).txt', 'r') as file:
    strings = file.readlines()

max_cnt = 0

for string in strings:
    for i in range(len(string)):
        if string[i - 1] != 'd' and string[i] != 'a' or string[i - 1] != 'a' and string[i] != 'd' or string[i + 1] != 'a' and string[i] != 'd' or string[i + 1] != 'd' and string[i] != 'a':
            max_cnt += 1
        else:
            max_cnt = 0
    print(max_cnt)
