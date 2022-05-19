import csv

numbers = []
first_num = 16
with open('18.csv', 'r', encoding='utf8') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read())
    csvfile.seek(0, 0)
    reader = csv.reader(csvfile, dialect=dialect)
    for row in reader:
        numbers.append(list(map(int, row)))

print(numbers)
for nums in numbers:
    for i in range(len(nums)):

