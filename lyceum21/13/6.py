import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 1800
a = 55
for teta in range(1,n,10):
    r = a * radians(teta) ** (-0.5)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
turtle.done()