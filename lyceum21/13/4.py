import turtle
from math import sin,cos, radians,exp

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 3600
a = 4
b = 0.15
for teta in range(0,n,10):
    r = a * exp(b*radians(teta))
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
turtle.done()
