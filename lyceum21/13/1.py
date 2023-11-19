import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')

a = 0
b = 10
for teta in range(1800):
    r = a + b * radians(teta)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
turtle.done()

