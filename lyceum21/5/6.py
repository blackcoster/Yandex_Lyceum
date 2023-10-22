a = int(input())
b = int(input())
if a>b:
    for i in range(a,b, -2):  # a=1 b-10
        print(i, end=' ')  # 1 4 7 10
else:
    for i in range(b,a, -2):  # a=1 b-10
        print(i, end=' ')  # 1 4 7 10
