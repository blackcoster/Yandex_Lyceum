start, stop, step = int(input()), int(input()), int(input())

if start < stop:
    for i in range(start, stop + 1, step):
        print(i, end=' ')
    print('Летим!')
elif stop == 0:
    for i in range(start, stop - 1, -step):
        print(i, end=' ')
    print('Сели!')
else:
    for i in range(start, stop - 1, -step):
        print(i, end=' ')
    print('Снизились.')
