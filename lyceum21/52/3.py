import turtle
from turtle import Screen, Turtle, done, addshape, onkey, listen


def func_pu_pd(x, y):
    global CLICK
    CLICK = not CLICK
    if CLICK:
        tom.pu()
    else:
        tom.pd()


def brush_width1():
    tom.pensize(1)


def brush_width2():
    tom.pensize(2)


def brush_width3():
    tom.pensize(3)


def brush_width4():
    tom.pensize(4)


def brush_width5():
    tom.pensize(5)


def brush_width6():
    tom.pensize(6)


def brush_width7():
    tom.pensize(7)


def brush_width8():
    tom.pensize(8)

def bg_white():
    turtle.bgcolor('white')
    tom.clear()


def bg_beige():
    turtle.bgcolor('beige')
    tom.clear()


def bg_corn():
    turtle.bgcolor('cornflowerblue')
    tom.clear()


def bg_yellow():
    turtle.bgcolor('yellow')
    tom.clear()


CLICK = False
sc = Screen()
sc.setup(startx=0, starty=0)
tom = Turtle()
tom.speed(0)
addshape('brush.gif')
tom.shape('brush.gif')
tom.ondrag(tom.goto)
tom.onclick(func_pu_pd, btn=3)
onkey(brush_width1, '1')
onkey(brush_width2, '2')
onkey(brush_width3, '3')
onkey(brush_width4, '4')
onkey(brush_width5, '5')
onkey(brush_width6, '6')
onkey(brush_width7, '7')
onkey(brush_width8, '8')

onkey(bg_white, 'w')
onkey(bg_beige, 'b')
onkey(bg_corn, 'c')
onkey(bg_yellow, 'y')

listen()
done()
