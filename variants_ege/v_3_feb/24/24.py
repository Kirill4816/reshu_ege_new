with open('24 (6).txt', 'r') as file:
    strings = file.read().split('A')

max_len_string = 0
for string in strings:
    if strings.count('E') >= 3:
        if len(string) > max_len_string:
            max_len_string = len(string)
print(max_len_string)

