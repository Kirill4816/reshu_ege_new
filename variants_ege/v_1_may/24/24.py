with open('24 (9).txt', 'r') as file:
    strings = file.read().split()

str_min_cnt_n = ''
min_cnt_G = 10000

for string in strings:
    cnt_G = string.count('G')
    if cnt_G < min_cnt_G:
        min_cnt_G = cnt_G
        str_min_cnt_n = string


letters = list(set(str_min_cnt_n))
letters.sort()

max_letter = ''
max_cnt_letter = 0

for letter in letters:
    count = str_min_cnt_n.count(letter)
    if count >= max_cnt_letter:
        max_cnt_letter = count
        max_letter = letter

print(max_letter)
