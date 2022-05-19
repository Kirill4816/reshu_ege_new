with open('24.txt', 'r') as file:
    string = file.read()

cnt_group = 0
strings = string.split('A')

for string in strings:
    if len(string) >= 10 and string.count('B') >= 2:
        cnt_group += 1
print(cnt_group - 1) # в strings[0] нет с краев а, поэтому ее не засчитываем

print(strings[0])
print(strings[-1])