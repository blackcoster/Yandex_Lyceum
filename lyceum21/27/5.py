from math import cos, sin, radians, pi
from turtle import Turtle, done

a1, a2 = [int(x) for x in input().split()]
c1, c2 = input().split()
heart1 = Turtle()
heart1.speed(0)
heart1.color(c1)
heart2 = Turtle()
heart2.speed(0)
heart2.color(c2)
m = 1
heart1.pu()
heart1.begin_fill()
heart2.pu()
heart2.begin_fill()
for t in range(361):
    x1 = a1 * (m + 1) * sin(radians(m * t)) - a1 * m * sin(radians(t + m * t))
    y1 = a1 * (m + 1) * cos(radians(m * t)) - a1 * m * cos(radians(t + m * t)) + 50
    heart1.goto(x1, y1)
    x2 = a2 * (m + 1) * sin(radians(m * t) + pi / 4) - a2 * m * sin(radians(t + m * t) + pi / 4) + 150
    y2 = a2 * (m + 1) * cos(radians(m * t) + pi / 4) - a2 * m * cos(radians(t + m * t) + pi / 4) - 80
    heart2.goto(x2, y2)

heart1.end_fill()
heart1.ht()
heart2.end_fill()
heart2.ht()
done()
