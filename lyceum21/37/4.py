n, m = [int(x) for x in input().split()]
data = []
for i in range(n, m + 1):
    temp = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            temp.append(j)
            if i // j != j:
                temp.append(i // j)
    if temp:
        temp.sort()
        data.append(temp)
with open('divisors.txt', 'w') as out_file:
    for line in data:
        for n in line:
            print(n, file=out_file, end=' ')
        print(file=out_file)