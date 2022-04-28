n = []
cnt_pairs = 0
for i in range(len(n)):
    for g in range(i + 6, len(n)):
        if abs(i - g) % 3 == 0:
            cnt_pairs += 1
print(cnt_pairs)
