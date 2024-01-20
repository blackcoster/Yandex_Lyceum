from math import cos, sin, radians, pi
from turtle import Turtle, done, colormode

n, a, step, r, g, b = [int(x) for x in input().split()]
hearts = [Turtle() for i in range(n)]
colormode(255)
colors = [(r - i * step, g - i * step, b - i * step) for i in range(n)]

for i in range(n - 1, -1, -1):
    hearts[i].speed(0)
    hearts[i].color(colors[i])
    hearts[i].pu()
    hearts[i].begin_fill()

hearts_a = [a + i * step for i in range(n)]
for t in range(361):
    for i in range(n):
        x = hearts_a[i] * 2 * sin(radians(t)) - hearts_a[i] * sin(radians(2 * t))
        y = hearts_a[i] * 2 * cos(radians(t)) - hearts_a[i] * cos(radians(2 * t))
        hearts[i].goto(x, y)
        hearts[i].pd()

for i in range(n):
    hearts[i].end_fill()
    hearts[i].ht()

done()
