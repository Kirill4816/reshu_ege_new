# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя
# одинаковыми символами.

with open('24 (1).txt', 'r') as file:
    strings = file.readlines()

letters = {}

for string in strings:
    for i in range(len(string) - 1):
        if string[i - 1] == string[i + 1]:
            if string[i] not in letters:
                letters[string[i]] = 1
            else:
                letters[string[i]] += 1
max_letter = max(letters.values())
print(max_letter)
