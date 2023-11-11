# n,m = int(input()), int(input())
#
# count = 0
# for i in range(n,m+1):
#     while i > 0:
#         if i%10 == 3:
#             count+=1
#         i//=10
# print()

# #2
# n,m = int(input()), int(input())
# if n>m:
#     n,m = m,n
# for i in range(n,m+1):
#     print(f'{i}:\t',end = '')
#     count = 0
#     for j in range(1,i+1):
#         if i % j ==0:
#             count += 1

#     print('*' * count)


#3
avg_max = 0
name_max = ''
for _ in range(int(input())):
    name = input()
    n = int(input())
    songs = 0
    for _ in range(n):
        songs += int(input())
    if songs/n > avg_max:
        avg_max = songs/n
        name_max = name
print(name)