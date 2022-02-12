with open('24 (4).txt', 'r') as file:
    strings = file.readlines()   # readline -> readlines, split don't used with arrays)

min_cnt_N = float('inf')   # TODO remember this expression
string_min_N = ''
letters = {}  # may be not used

for string in strings:
    if string.count('N') < min_cnt_N:
        min_cnt_N = string.count('N')
        string_min_N = string

most_freq_letter = ''
freq_count = 0

for i in range(ord('A'), ord('Z') + 1):
    letters[chr(i)] = 0   # ????  what is that
    cnt = string_min_N.count(chr(i))
    if cnt >= freq_count:  # >=   ->  the next letter is later in the alphabet, so it has priority
        freq_count = cnt
        most_freq_letter = chr(i)

print(most_freq_letter)