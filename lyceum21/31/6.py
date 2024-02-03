from math import sin, cos, radians
from turtle import Screen, Turtle, done

a = int(input())
sc = Screen()
sc.setup(7 * a, 7 * a, 0, 0)
sc.title('Persik')

peach = Turtle()
peach.speed(0)
peach.color('orange')
peach.begin_fill()
for t in range(361):
    x = 2 * a * sin(radians(t)) - a * sin(radians(2 * t))
    y = 2 * a * cos(radians(t)) - a * cos(radians(2 * t))
    peach.goto(x, y)
peach.end_fill()
peach.lt(90)
peach.color('brown')
peach.pensize(7)
peach.circle(3 * a, 30)
peach.ht()
done()
