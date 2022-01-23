first_num = 174457
second_num = 174505

for num in range(first_num, second_num + 1):
    dividers = []
    for div in range(2, num // 2 + 1):
        if num % div == 0:
            dividers.append(div)
        if len(dividers) > 2:
            break
    if len(dividers) == 2:
        print(f'{dividers[0]}\t\t{dividers[1]}')
