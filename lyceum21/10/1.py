# #таблица умножения
# for i in range(1,10):
#     for j in range (1,10):
#         print(f'{i} * {j} = { i * j}')
#     print()


# # таблица по горизоньали
# n = int(input())
# m = int(input())
#
# for i in range(n):
#     for j in range(m):
#         print(j + 1 + (i * m),end = '\t')
#     print()


# таблица по вертикали
n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        print(j*n + i +1,end = '\t')
    print()