with open('27-A (1).txt', 'r') as file:
    numbers = file.read().split()

numbers = tuple(map(int, numbers))

