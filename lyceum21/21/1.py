# a = (18,2,3,18)
# b = (18,)
#
#
# a = 1,2,3
# print(type(a))
#
# a, b = 3, 5
#
# a = [4,2,9,3,1]
#
# # 2 4 9 3 1
# # 2 4 3 9 1
# # 2 4 3 1 9
#
# n = len(a)
# for i in range(n-1):
#     for j in range(n-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
#
#
# from turtle import *
#
# section = Turtle()
# section.pensize(2)
# section.color('royalblue')
# section.speed(0)
# section.pu()
# section.goto(180, 0)
# a = section.pos()
# print(a)
#
#
# name = input()
# names = []
# while name:
#     names.append(name)
#     name = input()
# for i in range(len(names) - 1):
#     for j in range(len(names) - 1 - i):
#         if names[j] > names[j + 1]:
#             names[j], names[j + 1] = names[j + 1], names[j]
# for i in range(0, len(names), 2):
#     if len(names) % 2 and i == len(names) - 1:
#         print(names[i])
#     else:
#         print(f'{names[i]}, {names[i + 1]}')
#
from math import cos, radians
from turtle import Turtle, done

triangle = Turtle()
side, angle, n = int(input()), int(input()), int(input())
triangle.speed(1)
base = side * cos(radians(angle))

triangle.color('blue')
triangle.pu()
triangle.goto(base, -side / 2)
points = [triangle.pos()]
triangle.lt(180 - angle)
for _ in range(n):
    triangle.fd(side / n)
    points.append(triangle.pos())
triangle.lt(2 * angle)
for _ in range(n):
    triangle.fd(side / n)
    points.append(triangle.pos())

triangle.seth(0)
for i in range(0, len(points) // 2 + 1, 2):
    triangle.pu()
    triangle.goto(points[i])
    triangle.begin_fill()
    triangle.goto(points[len(points) - i - 1])
    triangle.goto(points[len(points) - i - 2])
    triangle.goto(points[i + 1])
    triangle.end_fill()
    triangle.pd()

triangle.hideturtle()
done()