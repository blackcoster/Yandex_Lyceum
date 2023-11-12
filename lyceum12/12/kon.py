x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if (x2-x1) * (y2-y1) == 2 or (x2-x1) * (y2-y1) == -2:
    print('Да')
else:
    print('Нет')


# 1 2
# 1 -2
# -1 2
# -1 -2
#
# 2 1
# 2 -1
# -2 1
# -2 -1