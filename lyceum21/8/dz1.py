# find = input()
# stroka = input()
# k = 0
# while stroka != 'Вот как!':
#     if find in stroka:
#         k += 1
#     stroka = input()
# print(k)


# n = int(input())
# while n>=10:
#     if len(str(n))==2:
#         if n%10 == n//10:
#             print(n)
#     if len(str(n))==4:
#         if n%10 == n//1000 and n//100 % 10==n//10 % 10:
#             print(n)
#     n = int(input())

# n = int(input())
# stroka = input()
# # same while stroka != ''
# i = 1
# while stroka:
#     if i % 2 == 1:
#         print(stroka)
#     else:
#         print(' ' * (n - len(stroka))+stroka)
#     i += 1
#     stroka = input()


# n= input()
# summa = 0
# while n:
#     n = int(n)
#     if n%10 !=0 and n%(n%10)==0:
#         summa+=n
#     n = input()
# print(summa)

float('inf')
a = 1
print(f'{a:.6f}')