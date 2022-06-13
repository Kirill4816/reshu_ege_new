with open('24_demo (1).txt', 'r') as file:
    string = file.read()

max_seq_len = 0
cur_seq_len = 0
previous = 'Z'

next_dict = {
    'X': 'Y',
    'Y': 'Z',
    'Z': 'X'
}

for symbol in string:
    if symbol == next_dict[previous]:
        cur_seq_len += 1
        previous = symbol
    else:
        previous = 'Z'
        if cur_seq_len > max_seq_len:
            max_seq_len = cur_seq_len
        cur_seq_len = 0

if cur_seq_len > max_seq_len:
    max_seq_len = cur_seq_len

print(max_seq_len)
