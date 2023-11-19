import turtle
from math import sin,cos, radians

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 720
a = 60
k = 0.3
number = 5
alpha = 360//number
for i in range(number):
    for teta in range(1,n,15):
        r = a * radians(teta) ** (-k)
        x = r * cos(radians(teta+i*alpha))
        y = r * sin(radians(teta+i*alpha))
        arch.goto(x,y)
    arch.pu()
    arch.home()
    arch.pd()
turtle.done()