with open('26 (1).txt', 'r') as file:
    numbers = list(map(int, file.read().split()))

cnt = numbers[0]
begin_lifting_capacity = numbers[1]
lifting_capacity = numbers[1]
weights = numbers[2:]
guaranteed_weight = 0
cnt_weights = 0

for weight in weights[:]:
    if 210 <= weight <= 220:
        cnt_weights += 1
        guaranteed_weight += weight
        weights.remove(weight)

lifting_capacity -= guaranteed_weight
weights.sort()
removed_weights = []
for weight in weights[:]:
    if lifting_capacity - weight >= 0:
        lifting_capacity -= weight
        removed_weights.append(weight)
        cnt_weights += 1
        weights.remove(weight)
    else:
        break
removed_weights = removed_weights[::-1]
for last_weight in removed_weights[:]:
    if lifting_capacity > 0:
        lifting_capacity -= last_weight
        for weight in weights[:]:
            if weight < lifting_capacity:
                removed_weights.remove(last_weight)
                weights.remove(weight)
                removed_weights.insert(0, weight)
                weights.insert(0, last_weight)
                last_weight = weight
            else:
                break
        lifting_capacity += last_weight

print(cnt_weights, begin_lifting_capacity - lifting_capacity)
