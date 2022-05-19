
def stones(cnt_stones, name_player, step, next_player, text):
    if step > 5:
        text += '\nболее 3х ходов'
        print(text)
        return
    if cnt_stones >= 11 and cnt_stones % 2 != 0:
        text += f'\nигрок {name_player} выиграл на {step} шаге с {cnt_stones * 2} камнями'
        print(text)
    steps = [cnt_stones + 1, cnt_stones + 2]
    if cnt_stones % 2 != 0:
        steps.append(cnt_stones * 2)
    for i in steps:
        if i >= 22:
            text += f'\nигрок {name_player} выиграл на {step} шаге с {i} камнями\n'
            print(text)
            return
    for v in steps:
        text += f'\nигрок {name_player} сделал из {cnt_stones} - {v} камней на {step} шаге'
        stones(v, next_player, step + 1, name_player, text)

for s in range(1, 11):
    print()
    print()
    print(f'сейчас {s} камней')
    stones(s, 'петя', 1, 'ваня', '')

