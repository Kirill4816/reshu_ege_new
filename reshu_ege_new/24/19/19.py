# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.

with open('24.txt') as file:
    text = file.read()
results = dict()
found = False
for letter in text:
    if found:
        if letter in results:
            results[letter] += 1
        else:
            results[letter] = 1
    if letter == 'E':
        found = True
    else:
        found = False

max_cnt_letter = 0
max_letter = ''
for letter, count in results.items():
    if count > max_cnt_letter:
        max_cnt_letter = count
        max_letter = letter

print(max_letter)
