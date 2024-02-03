n = int(input())
result = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    result.append(temp)

for j in range(len(result[0])):
    total = sum([result[i][j] for i in range(n)])
    print(total, end=' ')
