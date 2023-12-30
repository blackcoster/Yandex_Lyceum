import turtle
from math import radians, sin, pi, gcd

lissajous = turtle.Turtle()
lissajous.speed(0)
lissajous.pensize(3)
lissajous.color(input())
n = 360
r1, r2 = int(input()), int(input())
a, b = int(input()), int(input())
phi = pi / 2
k = gcd(a, b)

lissajous.pu()
lissajous.goto(0,abs(r2))
lissajous.write(f'a = {a}, b = {b}', align='center',
                font=('Times New Roman', 24, 'normal'))

for t in range(n // k + 1):
    x = r1 * sin((a * radians(t)) + phi)
    y = r2 * sin(b * radians(t))
    lissajous.goto(x,y)
    lissajous.pd()
lissajous.ht()
turtle.done()