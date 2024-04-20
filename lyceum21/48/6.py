from turtle import Turtle, Screen, done

def left(x,y):
    s.goto(x, y)
    s.pd()
    side = 3
    step = 1
    for _ in range(50):
        s.fd(side)
        s.lt(40)
        side += step
    s.pu()


def right(x,y):
    s.goto(x, y)
    s.pd()
    side = 3
    step = 1
    for _ in range(50):
        s.fd(side)
        s.rt(40)
        side += step
    s.pu()


s = Turtle()
sc = Screen()
sc.setup(startx=0,starty=0)
s.speed(0)
s.ht()
s.color('royalblue')
s.pensize(3)
s.pu()

sc.onclick(left,1)
sc.onclick(right,3)
sc.listen()
done()
