n = int(input())
s = 0
k = 0
while s < n:
    k += 1  # 1 2 3
    s += k  # 1, 1+2, 1+2+3
if s == n:
    print(k)
else:
    print('NO')
