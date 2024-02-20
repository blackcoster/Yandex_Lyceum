from turtle import *

frac = Turtle()
length_long = 300
size = 10
dot_size = 20
frac.color(input())
n = int(input())
points = [(0,0)]

for _ in range(n+1):
    length_short = length_long / 1.618
    frac.pensize(size)
    points1 = []
    for coords in points:
        frac.seth(0)
        frac.pu()
        frac.goto(coords)
        frac.pd()

        frac.back(length_long / 2)
        frac.lt(90)
        frac.fd(length_short / 2)

        # первая точка
        frac.dot(dot_size)
        points1.append(frac.pos())

        # вторая точка
        frac.back(length_short)
        frac.dot(dot_size)
        points1.append(frac.pos())

        # перекладина
        frac.fd(length_short / 2)
        frac.rt(90)
        frac.fd(length_long)
        frac.lt(90)
        frac.fd(length_short / 2)

        # третья точка
        frac.dot(dot_size)
        points1.append(frac.pos())
        frac.back(length_short)

        # четвертая точка
        frac.dot(dot_size)
        points1.append(frac.pos())
    points = points1.copy()
    length_long//=2
    size-=2
    dot_size-=2
frac.ht()
done()