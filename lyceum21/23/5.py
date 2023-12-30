import turtle
from math import radians, sin, pi, gcd,cos

lissajous = turtle.Turtle()
lissajous.speed(0)
lissajous.pensize(3)
colors = ('violet', 'crimson', 'orangered', 'orange', 'yellow')
n = 360
r1, r2 = int(input()), int(input())
b = 10
for a in range(2,11,2):

    lissajous.pu()
    lissajous.color(colors[a//2-1])
    for t in range(n // gcd(a,b) + 1):
        x = r1 * cos(a * radians(t))
        y = r2 * sin(b * radians(t))
        lissajous.goto(x,y)
        lissajous.pd()
lissajous.ht()
turtle.done()