#double spiral

import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')
arch.speed(9)
a = 40
k = 0.7
n = 720
for teta in range(n):
    r = a * radians(teta) ** k
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
arch.pu()
arch.goto(0,0)
arch.pd()
arch.color('blue')
a = -a
for teta in range(n):
    r = a * radians(teta) ** k
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
arch.ht()
turtle.done()
