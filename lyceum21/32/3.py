# snake

n, m = int(input()), int(input())
data = [[i + j * n + 1 for j in range(m)] for i in range(n)]

# отражение по вертикали
for i in range(n):
    for j in range(m // 2):
        data[i][j], data[i][m - j - 1] = data[i][m - j - 1], data[i][j]
# отражение по горизонтали
for i in range(n // 2):
    for j in range(m):
        data[i][j], data[n - i - 1][j] = data[n - i - 1][j], data[i][j]


for j in range(m - 2, -1, -2):
    column = [data[i][j] for i in range(n)]
    column.reverse()
    for i in range(n):
        data[i][j] = column[i]

for row in data:
    print('\t'.join([str(x) for x in row]))

