#таблица умножения

for i in range(1,10):
    if i == 3:
        continue
    for j in range (1,10):
        if j == 3:
            continue
        print(f'{i} * {j} = { i * j}')
    print()