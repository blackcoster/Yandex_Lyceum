# n = int(input())
# i = 1 # delitel
# while i <= n:
#     if n%i ==0:
#         print('delitel',i)
#     i+=1

n = int(input())
i = 1 # delitel
while i <= int(n**(0.5)):
    if n % i ==0:
        print('delitel 1 part = ',i)
        if n//i != i:
            print('delitel 2 part = ',n//i)
    i+=1