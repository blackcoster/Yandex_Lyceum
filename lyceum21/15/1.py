from turtle import Turtle, done

line = Turtle()
line.color('blue')
b = 20
for k in range(-12,13,3):
    x = -200
    y = k/10 * x + b
    line.pu()
    line.goto(x,y)
    line.pd()
    x = 200
    y = k / 10 * x + b
    line.goto(x,y)
line.ht()
done()

