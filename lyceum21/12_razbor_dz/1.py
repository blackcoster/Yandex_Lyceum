# 1
# from math import log
# a = int(input())
# n = int(input())
#
# print(round(log(a,n)))


#2
#from math import tan, radians
#
# x, y, alpha = float(input()), float(input()), int(input())
# k = tan(radians(alpha))
# b = y - k*x
#
# print(f'y = {round(k, 2)} x + {round(b, 2)}' if b > 0 else
#       f'y = {round(k, 2)} x - {round(abs(b), 2)}')



# #3
# from math import exp
#
# x = float(input())
# f1 = (0.2 * x) ** 3
# f2 = (0.2 * (x + 0.01)) ** 3
# g1 = exp(0.2 * x) - 1
# g2  = exp(0.2 * (x + 0.01)) - 1
#
# speed1 = (f2 - f1) / 0.01
# speed2 = (g2 - g1) / 0.01
# diff = abs(speed1 - speed2)
# if speed1 > speed2:
#     print('Первая')
# else:
#     print('Вторая')
# print(round(diff, 4))

#4
# from math import log
#
# mass_start = int(input())
# velocity = 0
# impact = input()
# while impact:
#     impact = int(impact)
#     stage = int(input())
#     velocity+=impact*log(mass_start/mass_start - stage*0.9)
#     mass_start -= stage
#     impact = input()
#
# print(round(velocity,2))

#5
# import random
# import string
# n, m, k = int(input()), int(input()), int(input())
# first = random.choice(string.ascii_uppercase)
# second = random.randrange(n,m,k)
# third = random.uniform(1,9)
#
# print(f'{first}-{second}-{third:.3f}')

#6
# from random import randint
# from turtle import Turtle, done
# c=Turtle()
# c.speed(0)
# a,b = int(input()), int(input())
# color = input()
# c.color(color)
# radius = randint(a,b)
# y = randint(-300,300-2*radius)
# c.pu()
# c.goto((0, y))
# c.pd()
# c.begin_fill()
# c.circle(radius)
# c.end_fill()
# c.hideturtle()
# done()

# #7 dop
# from math import acos, degrees
#
# a, b, c = float(input()), float(input()), float(input())
# value = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
# deg = degrees(acos(value))
# print(round(deg, 1))

##8 dop
# import random as rd
#
# r = 1000
# n = int(input())
# circle = 0
# for _ in range(n):
#     x, y = rd.randint(-r, r), rd.randint(-r, r)
#     if x ** 2 + y ** 2 <= r ** 2:
#         circle += 1
# print(4 * circle / n)


#vlozhennie zikli zmeika
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            print(i + 1 + n * j, end='\t')
        else:
            print(n * (j + 1) - i, end='\t')
    print()


#algoritmi
n = int(input())
s = 0
for i in range(2, n, 2):
    if n % i == 0:
        s += i
print(s)

#pesni
min_line = max_line = ''
line = input()
while line:
    if not min_line or min_line and line < min_line:
        min_line = line
    if not max_line or max_line and line > max_line:
        max_line = line
    line = input()
print(min_line)
print(max_line)

#yagodi
a, b = int(input()), int(input())
m, n = a, b
while m * n:
    m, n = n % m, m
gcd = m + n
print(gcd)
print(a // gcd, b // gcd)


#yama
b = int(input())
big_yama = b
a = int(input())
while a <= 100:
    if a < big_yama:
        print('Большая яма!')
        break
    if a < 0:
        print('ямка')
    elif a >= 0:
        print(a)
    a = int(input())


#not small
n = int(input())
m1 = m2 = 1_000_000
while n != 1_000_000:
    if n < m1:
        m2, m1 = m1, n
    elif n < m2:
        m2 = n
    n = int(input())
print(m2)

#skip
n = int(input())
s = 0
for _ in range(n):
    line = input()
    if (s + len(line)) % 3 == 0:
        print('Пропускаем')
        continue
    s += len(line)
    print(s)

#ritm
n, m, k = int(input()), int(input()), int(input())
a, b = n, m
while a * b:
    a, b = b, a % b
g = a + b
scm = n * m // g
print(scm * k)

#poidi
x, y = int(input()), int(input())
cur_x = cur_y = 0
while True:
    if x == cur_x and y == cur_y:
        print('Дошли!')
        break
    direction = input()
    step = int(input())
    if direction == '↑':
        cur_y += step
    elif direction == '↓':
        cur_y -= step
    elif direction == '→':
        cur_x += step
    elif direction == '←':
        cur_x -= step
    print(cur_x, cur_y)


#
m, h = int(input()), int(input())
search = False
for x in range(1, 1000):  # x - количество секунд в минуте
    for y in range(1, 1000):  # y - количество часов в сутках
        if m * x == h * y:  # количество секунд в сутках
            print(m * x)
            search = True
            break
    if search:
        break


#while
#koshki
n = int(input())
s = 0
f = 0
while n > 0:
    if n % 3 == 0 and n % 10 == 2:
        s += 1
    if 1000 > n > 99:
        f += 1
    n = int(input())
print(s)
if f > 0:
    print('ДА')
else:
    print('НЕТ')

#dom
line = input()
max_line = ''
while line != 'Который построил Джек.':
    if ' ' not in line:
        print(line)
    else:
        if len(line) > len(max_line):
            max_line = line
    line = input()
print(max_line)


#vsplivaem
from turtle import *
bubble = Turtle()
col1, col2 = 'maroon', 'wheat'
bubble.color(col1, col2)
w, r, n = int(input()), int(input()), int(input())
# bubble.speed(0)
bubble.pu()
bubble.goto(-1.5 * w, 2 * w)
bubble.pd()
bubble.begin_fill()
bubble.fd(3 * w)
bubble.rt(90)
bubble.pensize(6)
bubble.fd(4 * w)
bubble.rt(90)
bubble.fd(3 * w)
bubble.rt(90)
bubble.fd(4 * w)
bubble.rt(90)
bubble.end_fill()

bubble.pu()
y = -2 * w
bubble.goto(0, y)
bubble.pd()
bubble.color('steelblue', 'lightsteelblue')
while y + 2 * r <= 2 * w:
    bubble.pensize(n)
    bubble.begin_fill()
    bubble.circle(r)
    bubble.end_fill()
    y += 3 * r
    r += 10
    n -= 1
    bubble.pu()
    bubble.goto(0, y)
    bubble.pd()

# bubble.hideturtle()
done()



#for voronka
symbol = input()
n = int(input())
for i in range(n - 1):
    space = ' ' * i
    print(space + symbol + ' ' * (2 * (n - i - 1) - 1) + symbol)
print(' ' * (n - 1) + symbol)

# delenie
n, m = int(input()), int(input())
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        print(i, end=' ')

# stars

from turtle import *

star = Turtle()
x, y = int(input()), int(input())
n, color = int(input()), input()
star.pu()
star.goto(x, y)
star.pd()
star.color(color)
for _ in range(n):
    star.lt(72)
    star.fd(120)
    star.rt(144)
    star.fd(120)
    star.rt(144)
    star.fd(120)
    star.rt(144)
    star.fd(120)
    star.rt(144)
    star.fd(120)
    star.lt(144)
    star.pu()
    star.fd(120)
    star.pd()
done()


#for - jadina
result = ''
last = ''
for _ in range(int(input())):
    line = input()
    if line > last:
        if result == '':
            result = line
        else:
            result += f', {line}'
        print(result)

    else:
        print('Маловато!')
    last = line