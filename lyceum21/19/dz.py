#1

# al = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# for i in range(int(input())):
#     al -= set(input())
# if al:
#     for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         if ch in al:
#             print(ch,end='')
# else:
#     print('УМЕЮТ ВСЁ')
#2
# s = input()
# start = int(input())
# step = int(input())
# new = s[start-1::step]
# print(new)

#3
# s = input()
# cut = int(input())
# while s:
#     left = s[:cut]
#     s = s[cut:]
#     print(left, s)

#4
# s = input()
# n = int(input())
# print(s[-1::-n])

#5
# last_letter = ''
# for i in range(int(input())):
#     word = input()
#     last_letter += word[-1]
# print(last_letter[::-1])

#6

from turtle import *
c = Turtle()
r, h = int(input()),int(input())
pen, fill = input(), input()
# r = 150
# h = 220
# pen = 'red'
# fill = 'gold'
c.pu()
c.goto(-100,-100)
c.pd()
c.color(pen,fill)
c.pensize(2)
# c.speed(0)
c.begin_fill()
for _ in range(2):
    c.fd(1.72*r)
    c.lt(90)
    c.fd(h)
    c.lt(90)
c.end_fill()
c.rt(90)
c.begin_fill()
c.circle(r/2, 45)
c.circle(r,90)
c.circle(r/2, 45)
for _ in range(2):
    c.pu()
    c.circle(r/2,9)
    c.pd()
    c.circle(r/2, 9)
c.pu()
c.circle(r/2, 9)
for _ in range(10):
    c.pd()
    c.circle(r,4.5)
    c.pu()
    c.circle(r, 4.5)
for _ in range(2):
    c.pd()
    c.circle(r/2,9)
    c.pu()
    c.circle(r/2, 9)
c.pd()
c.end_fill()
c.pu()
c.goto(-100+1.72*r,-100+h)
c.seth(90)
c.pd()
c.begin_fill()
c.circle(r/2, 45)
c.circle(r,90)
c.circle(r/2, 90)
c.circle(r,90)
c.circle(r/2, 45)
c.end_fill()
c.ht()

done()
