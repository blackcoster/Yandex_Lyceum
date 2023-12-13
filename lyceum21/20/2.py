from turtle import *

colors = ['crimson', 'orange', 'gold',
          'greenyellow', 'skyblue', 'blue']
square = Turtle()
square.speed(0)
square.pu()
square.goto(0, -180)
for i in range(18):
    square.pd()
    square.color(colors[i % len(colors)])
    square.begin_fill()
    for _ in range(4):
        square.fd(50)
        square.lt(90)
    square.end_fill()
    square.lt(5)
    square.pu()
    square.fd(75)
    square.lt(15)
square.ht()
done()