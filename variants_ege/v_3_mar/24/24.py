with open('24 (10).txt', 'r') as file:
    letters = file.read()

cnt_letters = {}
max_cnt = 0
max_letter = "-1"

for i in range(1, len(letters) - 1):
    if letters[i - 1] == letters[i + 1]:
        if letters[i] in cnt_letters:
            cnt_letters[letters[i]] += 1
        else:
            cnt_letters[letters[i]] = 1
        if  cnt_letters[letters[i]] > max_cnt:
            max_cnt = cnt_letters[letters[i]]
            max_letter = letters[i]

print(max_letter)

