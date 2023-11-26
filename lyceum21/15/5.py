from math import sin
from turtle import Turtle, done

sea = Turtle()
sea.color('steelblue')
sea.pu()
sea.goto(-350, -300)
sea.pd()
sea.begin_fill()
for x in range(-350, 351, 10):
    y = 30 * sin(0.025 * x)
    sea.goto(x, y)
sea.goto(350, -300)
sea.goto(-350, -300)
sea.end_fill()
sea.hideturtle()
done()