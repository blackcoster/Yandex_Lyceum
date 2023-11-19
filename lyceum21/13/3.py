import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')

a = 0
b = 10
arch.speed(9)
arch.pu()
kol = 4
k = 360//kol
for phi in range(0,360,k):
    for teta in range(0,360,10):
        r = a + b * radians(teta)
        x = r * cos(radians(teta+phi))
        y = r * sin(radians(teta+phi))
        arch.goto(x,y)
        arch.dot()
turtle.done()
