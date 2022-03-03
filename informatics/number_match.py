numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
if numbers_1 & numbers_2:
    print(len(numbers_1 & numbers_2))
