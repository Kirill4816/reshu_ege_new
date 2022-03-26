with open("inf_22_10_20_24.txt", 'r') as file:
    strings = file.readlines()

cnt_str = 0
cnt_A = 0
cnt_E = 0
for string in strings:
    cnt_E = string.count('E')
    cnt_A = string.count('A')
    if cnt_E > cnt_A:
        cnt_str += 1
    cnt_A = 0
    cnt_E = 0
print(cnt_str)
