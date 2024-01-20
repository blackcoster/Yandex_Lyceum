from turtle import *
from math import cos, sin, radians

contour, fill = input().split()
a = int(input())
k = float(input())
n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
# [[1, 2], [1 2], [2 5],]
ts = [Turtle() for i in range(n)]

for i in range(n):
    ts[i].speed(0)
    ts[i].color(contour, fill)
    ts[i].pensize(3)
    ts[i].pu()
    ts[i].begin_fill()

for t in range(721):
    for i in range(n):
        x = a * (1 - cos(radians(k * t)) + sin(radians(k * t)) ** 2) * cos(radians(t)) + points[i][0]
        y = a * (1 - cos(radians(k * t)) + sin(radians(k * t)) ** 2) * sin(radians(t)) + points[i][1]
        ts[i].goto(x, y)
        ts[i].pd()

for i in range(n):
    ts[i].end_fill()
    ts[i].ht()
done()
