from turtle import Turtle, done,bgcolor, colormode
r, g, b = [int(x) + 40 for x in input().split()]
r1, g1, b1 = [int(x) + 40 for x in input().split()]
bgcolor('#03a')
sun = Turtle()
sun.speed(5)
colormode(255)
sun.pu()
sun.goto(-40, -310)
sun.pd()
radius = 330
for _ in range(4):
    sun.lt(90)
    sun.color(r, g, b)
    sun.begin_fill()
    sun.circle(radius)
    sun.end_fill()
    r -= 10
    g -= 10
    b -= 10
    radius -= 10
    sun.rt(90)
    sun.bk(10)
sun.pu()
sun.goto(370, -190)
sun.pd()
radius1 = 190
for _ in range(4):
    sun.color(r1, g1, b1)
    sun.begin_fill()
    sun.circle(radius1)
    sun.end_fill()
    r1 -= 10
    g1 -= 10
    b1 -= 10
    radius1 -= 10
    sun.rt(90)
    sun.bk(10)
    sun.lt(90)

sun.ht()
done()