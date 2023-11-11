x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if x2 - x1 == y2 - y1 or x1 - x2 == y2 - y1:
    print('Да')
else:
    print('Нет')