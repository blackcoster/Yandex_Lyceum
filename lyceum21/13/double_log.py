import turtle
from math import sin,cos, radians,exp

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 720
a = 20
b = 0.21
for teta in range(0,n,10):
    r = a * exp(b*radians(teta))
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
arch.pu()
arch.goto(0,0)
arch.pd()
arch.color('blue')
a = -a
for teta in range(0,n,10):
    r = a * exp(b*radians(teta))
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
turtle.done()
