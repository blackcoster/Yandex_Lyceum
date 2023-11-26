from turtle import Turtle, done

line = Turtle()
line.color('blue')
k = 0.8
for b in range(-50, 51, 20):
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