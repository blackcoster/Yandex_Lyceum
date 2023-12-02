#1
age = int(input())
if age <= 13:
    print('Группа 1')
elif age <= 24:
    print('Группа 2')
elif age <= 59:
    print('Группа 3')
else:
    print('Группа 4')

#2
n, r = int(input()), int(input())
if n > r:
    print('Никита')
elif r > n:
    print('Родион')
else:
    print('Ничья')

#3
date = input()
if date == 'пн' or date == 'чт':
    print('Саша')
elif date == 'вт' or date == 'пт':
    print('Маша')
elif date == 'ср':
    print('Лёша')
else:
    print('Выходной')

#4
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

#5
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num2 < num1 < num3 or num3 < num1 < num2:
    print(num1)
elif num1 < num2 < num3 or num3 < num2 < num1:
    print(num2)
else:
    print(num3)

#6
step = int(input())
if step >= 10000:
    print('Молодец!')
elif step >= 5000:
    print('Неплохо')
else:
    print('Ты можешь больше!')


#7
m = int(input())
if m == 2:
    print(28)
elif m == 4 or m == 6 or m == 9 or m == 11:
    print(30)
else:
    print(31)

#8
m = int(input())
if 3 <= m <= 5:
    print('Весна')
elif 6 <= m <= 8:
    print('Лето')
elif 9 <= m <= 11:
    print('Осень')
else:
    print('Зима')

#9
num = int(input())
if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')
else:
    print('Ошибка')


