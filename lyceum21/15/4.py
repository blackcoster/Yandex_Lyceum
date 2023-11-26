from turtle import Turtle, done

seagull = Turtle()
seagull.color('dimgray', 'azure')

a, c, shift = -0.0025, 200, 100
seagull.pu()
seagull.goto(-300, a * (-300 + shift) ** 2 + c)
seagull.pd()
# 1 arc
seagull.begin_fill()
for x in range(-300, -1, 10):
    y = a * (x + shift) ** 2 + c
    seagull.goto(x, y)
# 2 arc
a, c, shift = -0.0025, 200, -100
for x in range(0, 301, 10):
    y = a * (x + shift) ** 2 + c
    seagull.goto(x, y)
# 3 arc
a, c, shift = -0.0015, 160, -100
for x in range(300, -1, -10):
    y = a * (x + shift) ** 2 + c
    seagull.goto(x, y)
# 4 arc
a, c, shift = -0.0015, 160, 100
for x in range(0, -301, -10):
    y = a * (x + shift) ** 2 + c
    seagull.goto(x, y)
seagull.end_fill()
seagull.hideturtle()
done()