from math import cos, exp
from turtle import Turtle, done

c = Turtle()
c.color(input())
c.pu()
a = a0 = float(input())
c.goto(-350, a0)
c.pd()
w = float(input())
t = 1

for x in range(-350, 351):
    y = a * cos(w * x)
    c.goto(x, y)
    a = a0 * exp(-0.005 * t)
    t += 1
c.ht()
done()
