# Системный администратор раз в неделю создаёт архив пользовательских файлов.
# Однако объём диска, куда он помещает архив, может быть меньше,
# чем суммарный объём архивируемых файлов.
# Известно, какой объём занимает файл каждого пользователя.
# По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске
# определите максимальное число пользователей,
# чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося файла,
# который может быть сохранён в архиве, при условии,
# что сохранены файлы максимально возможного числа пользователей.

with open("26 (2).txt", 'r') as file:
    numbers = file.read().split('\n')

empty_space = int(numbers[0].split(' ')[0])
sizes = numbers[1:]
sizes = list(map(int, sizes))

sizes.sort()
size = 0
previous_size = 0
count = 0

for current_size in sizes:
    if size + previous_size < empty_space:
        count += 1
        previous_size = current_size
        size += previous_size
    else:
        size -= previous_size
        break
print(count, end=' ')

sizes.reverse()
for current_size in sizes:
    if size + current_size <= empty_space:
        print(current_size)
        break
