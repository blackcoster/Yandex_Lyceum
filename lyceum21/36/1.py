from turtle import *

n = int(input())
frac = Turtle()
size = 10
length = 300
frac.color('maroon')
frac.pensize(size)
frac.pu()
frac.goto(0, -300)
frac.lt(90)
frac.pd()
# 0 итерация
frac.fd(length)
points = [{'xy': frac.pos(),
           'angle': frac.heading()}]
# 1 итерация
for _ in range(n):
    size -= 1
    length //= 2
    points1 = []
    for item in points:
        frac.pensize(size)
        for angle in -45, 45:
            frac.pu()
            frac.goto(item['xy'])
            frac.pd()
            frac.seth(item['angle'] + angle)
            frac.fd(length)
            points1 += [{'xy': frac.pos(), 'angle': frac.heading()}]
    points = points1.copy()

frac.ht()
done()