import turtle
from math import sin,cos, radians,exp,pi,sqrt

arch = turtle.Turtle()
arch.color('darkmagenta')
n = 720
a = 7.8
phi = (sqrt(5)+1)/2
for teta in range(0,n,10):
    r = a * phi**(2*radians(teta)/pi)
    x = r * cos(radians(teta))
    y = r * sin(radians(teta))
    arch.goto(x,y)
turtle.done()
