line = input().split()
result = []
for i in range(len(line)):
    if len(line[i]) > i:
        result.append(line[i][i])
    else:
        result = ['МАЛОВАТО']
print(''.join(result))

