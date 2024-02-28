import json
from turtle import Turtle, done

ann = Turtle()
bob = Turtle()
bgcolor('black')
shapes = turtles()
with open('colors.json') as file:
    colors = json.load(file)
for i in range(2):
    shapes[i].color(colors[i])
    shapes[i].speed(0)
    shapes[i].pensize(2)
    shapes[i].ht()
for step in range(3, 200):
    if step % 2:
        shapes[0].pd()
        shapes[1].pu()
    else:
        shapes[1].pd()
        shapes[0].pu()
    for i in range(2):
        shapes[i].fd(step)
        shapes[i].lt(61)

done()