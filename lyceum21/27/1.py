from turtle import *
from math import cos, sin, radians

curve = Turtle()
curve.speed(0)
contour, fill = input().split()
curve.color(contour, fill)
curve.pensize(3)
a, k = [int(x) for x in input().split()]
curve.pu()
curve.begin_fill()
for t in range(721):
    x = a * sin(radians(k * t)) * cos(radians(t))
    y = a * sin(radians(k * t)) * sin(radians(t))
    curve.goto(x, y)
    curve.pd()
curve.end_fill()
done()
