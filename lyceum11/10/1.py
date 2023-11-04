# month = int(input())
# if 5 <= month <= 7:
#     print('spring')
#
a = 8
b = 6
c = 8
# if (a == b == c):
#     print('equal')

# if (a>b):
#     print('>')
# elif (b>a):
#     print('<')
# else:
#     print('=')
#
if a>b:
    print('>')
else:
    if a<b:
        print('<')
    else:
        print('=')


a = 3
b=-6
c=6

summa = 0
if a>0:
    summa = summa+a
    # summa += a -----same!
if b>0:
    summa+=b
if c>0:
    summa+=c