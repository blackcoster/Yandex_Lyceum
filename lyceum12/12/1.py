num1 = 17
num2 = 18
if num1 // 3 < 5 or num1 > num2 and num2 % 3 == 0:
    print('Да')
else:
    print('Нет')

#
x = int(input())
if 5 <= x <= 9 or 26 <= x <= 30:
    print('Да')
else:
    print('Нет')

h = int(input())
m = int(input())
if h == 15 and (m == 0 or m == 30):
    print('Да')
else:
    print('Нет')

age = int(input())
want = input()
if age>=18 and want=='Да':
    print('Подходит')
else:
    print('Не подходит')