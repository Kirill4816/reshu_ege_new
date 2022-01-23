with open('27880.txt', 'r') as file:
    f = file.read().split()

numbers = list(map(int, f))
empty_size = numbers[0]
cnt_users = numbers[1]
numbers = numbers[2:]
numbers.sort()

cnt = 0
previous_size = 0

for num in numbers:
    if empty_size - num >= 0:
        cnt += 1
        empty_size -= num
        previous_size = num
    else:
        empty_size += previous_size
        break

numbers.sort(reverse=True)
for num in numbers:
    if empty_size - num >= 0:
        print(num)
        break
print(cnt)
