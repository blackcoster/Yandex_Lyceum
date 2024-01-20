from turtle import *
from math import cos, sin, radians, pi

colors = input().split()
a = int(input())
cycl, wheel = Turtle(), Turtle()
cycl.speed(0)
wheel.speed(0)
cycl.color(colors[0])
wheel.color(colors[1])
cycl.pu()
wheel.pu()
cycl.pensize(4)
point = -3 * pi * a, 0
cycl.goto(point)
wheel.goto(point)

for t in range(0, 360 * 3 + 1, 20):
    x = a * (radians(t) - sin(radians(t))) + point[0]
    y = a * (1 - cos(radians(t))) + point[1]
    cycl.goto(x, y)
    wheel.goto(x, 0)
    wheel.pd()
    cycl.dot(6)
    wheel.circle(a)

cycl.ht()
wheel.ht()
done()
