with open('24 (4).txt', 'r') as file:
    strings = file.readline().split()

min_cnt_N = 1000000
string_min_N = ''
letters = {}

for string in strings:
    if string.count('N') < min_cnt_N:
        min_cnt_N = string.count('N')
        string_min_N = string


for i in range(ord('A'), ord('Z') + 1):
    letters[chr(i)] = 0