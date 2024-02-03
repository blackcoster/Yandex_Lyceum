n, m = [int(x) for x in input().split()]
result = []

for i in range(n):
    temp = [input() for _ in range(m)]
    result.append(temp)
x, y = [int(x) - 1 for x in input().split()]

for i in range(n):
    for j in range(m):
        print(result[i][j], end='\t')
    print()
print(result[x][y])
