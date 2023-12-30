import turtle
from math import radians, sin, pi, gcd

lissajous = turtle.Turtle()
lissajous.speed(0)
lissajous.pensize(3)
colors = ('plum', 'crimson', 'orange', 'seagreen', 'blue')
n = 360
r1, r2 = int(input()), int(input())
a, b = 5,5
phi = pi / 2
k = gcd(a, b)

for i in range(5):
    phi = i * pi/8
    lissajous.pu()
    lissajous.color(colors[i])
    for t in range(n // k + 1):
        x = r1 * sin((a * radians(t)) + phi)
        y = r2 * sin(b * radians(t))
        lissajous.goto(x,y)
        lissajous.pd()
lissajous.ht()
turtle.done()