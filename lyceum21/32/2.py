#zerkalo
data = []
line = input()
while line:
    data.append([int(x) for x in line.split()])
    line = input()

# for i in range(len(data)):
#     data[i] = data[i][::-1]

for j in range(len(data[0])):
    for i in range(len(data) // 2):
        data[i][j], data[len(data) - 1 - i][j] = data[len(data) - 1 - i][j], data[i][j]

for row in data:
    print(row)