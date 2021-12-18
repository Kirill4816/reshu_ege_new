with open('inf_26_04_21_26.txt', 'r') as file:
    numbers = file.readlines()

first = True
cnt_dif_pair = 0
for num in numbers:
    if first:
        first = False
        continue
    num = num.split()
    num = tuple(map(int, num))
    if num[0] % 2 == 0 and num[1] % 2 != 0 or num[0] % 2 != 0 and num[1] % 2 == 0:
        cnt_dif_pair += 1
