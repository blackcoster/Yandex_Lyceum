#all flags

n = int(input())
m = int(input())
data = [['-'] * m for _ in range(n)]

k = int(input())
for _ in range(k):
    x,y = [int(a) for a in input().split()]
    data[x][y] = '\u2690'

data.insert(0,['-']*m)
data.append(['-']*m)
for row in data:
    row.insert(0,'-')
    row.append('-')

for i in range(1, n+1):
    for j in range(1, m+1):
        neighbors = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j),
                     (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        count = [1 for x, y in neighbors if data[x][y]=='\u2690']
        data[i][j] = sum(count) if count and data[i][j] != '\u2690' else data[i][j]
for i in range(1,n+1):
    for j in range(1,m+1):
        print(data[i][j], end = ' ')
    print()