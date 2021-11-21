with open('A.txt', 'r') as file:
    numbers = file.read().split()
    numbers = tuple(map(int, numbers))

print(numbers)
cnt = numbers[0]
numbers = numbers[1:]
digits = [0] * 120
first = 0
second = 0
for num in numbers:
    digit = num % 120
    if digit == 0:
        if digits[0] > num and digits[0] + num > first + second:
            first = digits[0]
            second = num
    else:
        if digits[120 - digit] > num and digits[120 - digit] + num > first + second:
            first = digits[120 - digit]
            second = num
    if num > digits[digit]: digits[digit] = num
print(first, second)
