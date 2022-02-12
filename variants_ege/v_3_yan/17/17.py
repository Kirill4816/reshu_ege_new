with open('17 (9).txt', 'r') as file:
    numbers = file.read().split()

numbers = list(map(int, numbers))
cnt_triples = 0
max_sum_triples = 0
for i in range(0, len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]
    max_angle = max([a, b, c])
    min_angle = min([a, b, c])
    mid_angle = sum([a, b, c]) - max_angle - min_angle
    if max_angle ** 2 == min_angle ** 2 + mid_angle ** 2:
        cnt_triples += 1
        if sum([a, b, c]) > max_sum_triples:
            max_sum_triples = sum([a, b, c])
print(cnt_triples, max_sum_triples)
