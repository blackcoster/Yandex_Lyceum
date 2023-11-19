n = int(input())
f = 1
s = 1
k = 2
if n ==1:
    print('1/2')
else:
    while s<n:
        f,s = s,f+s
        k+=1
        if s == n:
            print(f'eto {k}- chislo')
    if s>n:
        print('not fib')
# 1 1
# 1 2
# 2 3
# 3 5
