#double spiral

import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')
arch.speed(9)
a = 0
b = 10
n = 3 * 360
for teta in range(n):
    r = a + b * radians(teta)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
arch.pu()
arch.goto(0,0)
arch.pd()
arch.color('blue')
a = -a
for teta in range(n):
    r = a - b * radians(teta)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
arch.ht()
turtle.done()
