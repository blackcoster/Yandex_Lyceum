n = int(input())
field = [[0]*n for _ in range(n)]

for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    field[y][x] = 1

for i in range(n):
    for j in range(n):
        print(field[i][j], end=' ')
    print()
