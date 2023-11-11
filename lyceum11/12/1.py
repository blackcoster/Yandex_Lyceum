# num1 = 17
# num2 = 18
# if num1 // 3 < 5 or num1 > num2 and num2 % 3 == 0:
#     print('Да')
# else:
#     print('Нет')

# x = int(input())
# if 5<=x<=9 or 26<=x<=30:
# # if  x>= 5 and x<=9 or
#     print('Да')
# else:
#     print('Нет')


# hours = int(input())
# mins = int(input())
#
# if hours==15 and (mins == 0 or mins==30):
#     print('Да')
# else:
#     print('Нет')


# age = int(input())
# want = input()
#
# if age>=18 and want =='Да':
#     print('Подходит')
# else:
#     print('Нетё подходит')

#ладья
# x1 =int(input())
# y1 =int(input())
# x2 =int(input())
# y2 =int(input())
# if x1==x2 or y1==y2:
#     print('Да')
# else:
#     print('Нет')

#король
# x1 =int(input())
# y1 =int(input())
# x2 =int(input())
# y2 =int(input())
# if -1<=(x2-x1)<=1 and -1<=(y2-y1)<=1:
#     print('Да')
# else:
#     print('Нет')

#слон
# x1 =int(input())
# y1 =int(input())
# x2 =int(input())
# y2 =int(input())
# if x2-x1 == y2-y1 or x1-x2 == y2-y1:
#     print('Да')
# else:
#     print('Нет')

#конь
# x1 =int(input())
# y1 =int(input())
# x2 =int(input())
# y2 =int(input())
# if (x2-x1) * (y2-y1) == 2 or (x2-x1) * (y2-y1) == -2 :
#     print('Да')
# else:
#     print('Нет')

# ферзь
x1 =int(input())
y1 =int(input())
x2 =int(input())
y2 =int(input())
if x1==x2 or y1==y2 or x2-x1 == y2-y1 or x1-x2 == y2-y1:
    print('Да')
else:
    print('Нет')


hours = int(input())
minutes = int(input())
if (hours == 10 or hours == 11) and minutes == 30:
    print('Да')
else:
    print('Нет')


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 == (x2+y2) & 2:
    print('Да')
else:
    print('Нет')