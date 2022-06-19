with open('24 (11).txt', 'r') as file:
    strings = file.read().split('A')

strings = strings[1:-1]
cnt = 0

for string in strings:
    if len(string) >= 10 and string.count('B') >= 2:
        cnt += 1

print(cnt)
