from math import cos, sin, radians
from turtle import Turtle, done

colors = input().split()
contour = input()
a = int(input())
rose, stem = Turtle(), Turtle()
rose.speed(0)
stem.speed(0)
rose.pu()
stem.pu()
rose.pensize(3)
stem.pensize(4)
stem.color('darkgreen')
point = 0, -200
k = 5
i = 0

for angle in (0, -30, -60):
    stem.goto(point)
    stem.seth(0)
    stem.pd()
    stem.lt(90 + angle)
    stem.circle(500, 40)
    center = stem.pos()
    rose.goto(center)
    rose.color(contour, colors[i])
    rose.begin_fill()
    for t in range(181):
        x = a * sin(radians(k * t)) * cos(radians(t)) + center[0]
        y = a * sin(radians(k * t)) * sin(radians(t)) + center[1]
        rose.goto(x, y)
        rose.pd()
    rose.end_fill()
    stem.pu()
    rose.pu()
    i += 1
rose.ht()
stem.ht()
done()
