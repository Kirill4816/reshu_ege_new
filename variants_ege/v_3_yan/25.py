# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [245690; 245756] простые числа.
# Выведите на экран все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его порядковый номер в последовательности.
# Каждая пара чисел должна быть выведена в отдельной строке.

first_number = 245690
second_number = 245756
for idx, number in enumerate(range(first_number, second_number + 1)):
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            break
        if divider == number // 2:
            print(f'{idx + 1}\t\t{number}')
