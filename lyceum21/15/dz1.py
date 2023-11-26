from turtle import Turtle, done

sea = Turtle()
sea.color('rosybrown')
a, b, c, step = float(input()), float(input()), int(input()), int(input())
n = 1

while n <= 5:
    sea.pu()
    for x in range(-150, 141, 10):
        y = a * x ** 2 + b * x + c
        sea.goto(x, y)
        sea.pd()
    c += step
    n += 1

sea.hideturtle()
done()
