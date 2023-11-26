from math import cos, sin
from turtle import Turtle, done

island = Turtle()
island.speed(0)
sun, waves, land, tree, leaves = input(), input(), input(), input(), input()
island.color(sun)
island.pu()
island.goto(-150, 0)
island.pd()
island.begin_fill()
for x in range(-150, 151, 5):
    y = (150 ** 2 - x ** 2) ** 0.5
    island.goto(x, y)
island.goto(-150, 0)
island.end_fill()

island.color(waves)
island.pu()
island.goto(-350, -300)
island.pd()
island.begin_fill()
for x in range(-350, 351, 5):
    y = 10 * sin(0.144 * x) + 10
    island.goto(x, y)
island.goto(350, -300)
island.goto(-350, -300)
island.end_fill()

island.color(land)
island.pu()
island.goto(-100, -105)
island.pd()
island.begin_fill()
for x in range(-100, 201, 5):
    y = -0.0025 * (x - 50) ** 2 - 50
    island.goto(x, y)
for x in range(200, -101, -5):
    y = 0.0005 * (x - 50) ** 2 - 118
    island.goto(x, y)
island.end_fill()

island.color(tree)
island.pu()
island.goto(-8, 206)
island.pd()
island.begin_fill()
for x in range(-8, 81):
    y = 80 * (80 - x) ** 0.3 - 100
    island.goto(x, y)
for x in range(30, -9, -1):
    y = 50 * (30 - x) ** 0.5 - 100
    island.goto(x, y)
island.end_fill()

island.color(leaves)
island.pu()
island.goto(-40, 138)
island.pd()
island.begin_fill()
for x in range(-40, 21):
    y = 0.002 * (x + 8) ** 3 + 206
    island.goto(x, y)
for x in range(20, -41, -1):
    y = 2.05 * x + 221
    island.goto(x, y)
island.end_fill()

island.pu()
island.goto(-52, 258)
island.pd()
island.begin_fill()
for x in range(-52, -7):
    y = -0.0195 * (x + 60) ** 2 + 260
    island.goto(x, y)
for x in range(-8, -53, -1):
    y = 0.02 * x ** 2 + 205
    island.goto(x, y)
island.end_fill()
island.hideturtle()
done()