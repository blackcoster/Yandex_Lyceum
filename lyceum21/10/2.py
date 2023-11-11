num = int(input())
m = int(input())


for i in range(num//m):
    if i%2==0:
        for j in range(m):
            print(num - j, end = '\t')
        num-= 2 * m - 1
    else:
        for j in range(m,0,-1):
            print(num + m - j, end='\t')
        num -= 1
    print()

