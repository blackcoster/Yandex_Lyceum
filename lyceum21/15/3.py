from math import cos, exp
from turtle import Turtle, done

line = Turtle()
line.color(input())
a = a0 = float(input())
# delta = 0.28
line.pu()
t = 1
w = float(input())
for x in range(-350,351):
    y = a * cos(w * x)
    line.goto(x,y)
    line.pd()
    a = a0 * exp(-0.005 * t)
    t += 1
line.ht()
done()
