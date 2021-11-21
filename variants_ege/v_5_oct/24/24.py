file = open('24.txt')
str_min_cnt_n = ''
min_cnt_N = 10000
for line in file.readlines():
    cnt_n = line.count('N')
    if cnt_n < min_cnt_N:
        min_cnt_N = cnt_n
        str_min_cnt_n = line
file.close()

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
