from turtle import Turtle, done, Screen, colormode
import random


def draw(x, y):
    colormode(255)
    t.color((random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)))
    t.pu()
    t.goto(x + 40, y - 40)
    t.pd()
    t.begin_fill()
    for _ in range(4):
        t.lt(90)
        t.fd(80)
    t.end_fill()


t = Turtle()
t.ht()
t.speed(0)
sc = Screen()
sc.setup(starty=0, startx=0)
sc.onclick(draw)
sc.listen()
done()
