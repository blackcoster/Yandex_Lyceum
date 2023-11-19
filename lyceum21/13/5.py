import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 3600
a = 40
for teta in range(0,n,10):
    r = a * radians(teta) ** 0.5
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
    arch.dot()
turtle.done()