# Найдите все натуральные числа, принадлежащие отрезку [45000000;50000000],
# у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.

first_number = 45000000
second_number = 50000000
for number in range(first_number, second_number + 1):
    dividers = []
    for divider in range(1, number + 1):
        if divider % 2 != 0:
            if number % divider == 0:
                dividers.append(divider)
    if len(dividers) == 5:
        print(list.sort(dividers))
