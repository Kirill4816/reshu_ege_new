numbers = map(int, input().split())
numbers_set = set(numbers)

for number in numbers:
    if numbers in numbers_set:
        print('YES')
    else:
        print('NO')
        numbers_set.add(number)
