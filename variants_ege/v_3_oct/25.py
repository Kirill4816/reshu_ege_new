# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [2422000; 2422080],
# простые числа. Выведите все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его номер по порядку.

first_number = 2422000
second_number = 2422080
num_result = 0
for index, number in enumerate(range(first_number, second_number + 1)):
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            break
        if divider == number // 2:
            num_result += 1
            print(f'{num_result}\t\t{number}')
