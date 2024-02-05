# diag

data = []
line = input()
while line:
    data.append([int(x) for x in line.split()])
    line = input()
for i in range(len(data)):
    for j in range(i, len(data[0])):
        data[i][j], data[j][i] = data[j][i], data[i][j]
for row in data:
    print('\t'.join([str(x) for x in row]))
