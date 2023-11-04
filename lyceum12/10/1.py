month = int(input())
if 5 <= month <= 7:
    print('spring')

# a,b,c
#
# a<b, b<c -> a<c
# транзитивность
#
# a==b, b==c -> a==c

a, b, c = 3, 3, 3
#
if a == b == c:
    print('equal')
# a,b,c = 5,6,5
#
# a!=b, b!=c -> a!=c  ------ НЕ ТРАЗИТИВЕН

# a, b, c = 3, 6, 3
# #
# if a != b != c:
#     print('not equal')  --- РАБОТАЕТ НЕПРАВИЛЬНО