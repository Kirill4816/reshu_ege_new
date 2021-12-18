# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы A.

with open('24.txt', 'r') as file:
    strings = file.readlines()

letters = {}

for i in range(ord('A'), ord('Z') + 1):
    letters[chr(i)] = 0
print(letters)

max_letter = ''
max_value = 0

for string in strings:
    for i in range(len(string)):
        if string[i] == 'A':
            letters[string[i + 1]] += 1

for letter, value in letters.items():
    if value > max_value:
        max_value = value
        max_letter = letter

print(max_letter)
