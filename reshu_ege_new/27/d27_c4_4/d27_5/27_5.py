with open('27_5.txt', 'r', encoding='UTF-8') as file:
    numbers = file.readlines()

quart_1 = 0
quart_2 = 0
quart_3 = 0
quart_4 = 0
min_point_quart_1 = ()
min_point_quart_2 = ()
min_point_quart_3 = ()
min_point_quart_4 = ()
quarter_num = 0
cnt_points_quarter = 0
min_quarter_q_1 = float('inf')
min_quarter_q_2 = float('inf')
min_quarter_q_3 = float('inf')
min_quarter_q_4 = float('inf')
min_quarter = ()
min_point_axis = 0
min_len_axis = 0

for string in numbers[1:]:
    x, y = tuple(map(int, string.split()))
    if x > 0 and y > 0:
        quart_1 += 1
        if x < min_quarter_q_1 or y < min_quarter_q_1:
            min_quarter_q_1 = min([abs(x), abs(y)])
            min_point_quart_1 = (x, y)
    if x < 0 and y > 0:
        quart_2 += 1
        if x < min_quarter_q_2 or y < min_quarter_q_2:
            min_quarter_q_2 = min([abs(x), abs(y)])
            min_point_quart_2 = (x, y)
    if x < 0 and y < 0:
        quart_3 += 1
        if x < min_quarter_q_3 or y < min_quarter_q_3:
            min_quarter_q_3 = min([abs(x), abs(y)])
            min_point_quart_3 = (x, y)
    if x > 0 and y < 0:
        quart_4 += 1
        if x < min_quarter_q_4 or y < min_quarter_q_4:
            min_quarter_q_4 = min([abs(x), abs(y)])
            min_point_quart_4 = (x, y)

cnt_points_quarter = max([quart_1, quart_2, quart_3, quart_4])
if cnt_points_quarter == quart_1:
    quarter_num = 1
    min_point_axis = min_point_quart_1
    min_len_axis = min_quarter_q_1
if cnt_points_quarter == quart_2:
    quarter_num = 2
    min_point_axis = min_point_quart_2
    min_len_axis = min_quarter_q_2
if cnt_points_quarter == quart_3:
    quarter_num = 3
    min_point_axis = min_point_quart_3
    min_len_axis = min_quarter_q_3
if cnt_points_quarter == quart_4:
    quarter_num = 4
    min_point_axis = min_point_quart_4
    min_len_axis = min_quarter_q_4
print('K =', quarter_num)
print('M =', cnt_points_quarter)
print('A =', min_point_axis)
print('R =', min_len_axis)
