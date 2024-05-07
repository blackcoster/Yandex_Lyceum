from turtle import Turtle, Screen, done, addshape, onkey, listen, bgcolor


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
    bgcolor('white')
    tom.clear()


def bg_beige():
    bgcolor('beige')
    tom.clear()


def bg_corn():
    bgcolor('cornflowerblue')
    tom.clear()


def bg_yellow():
    bgcolor('yellow')
    tom.clear()


def check(w, h):
    x = (w + 150) // 50
    if -250 <= h <= -200 and 0 <= x <= 5:
        tom.pencolor(colors[int(x)])


CLICK = False
Screen().setup(startx=0, starty=0)
pal = Turtle()
pal.ht()
pal.speed(0)
pal.pu()
pal.goto(-150, -200)
pal.pensize(4)
colors = ['red', 'gold', 'green', 'blue', 'violet', 'brown']
for i in range(6):
    pal.color('black', colors[i])
    pal.begin_fill()
    pal.pd()
    for _ in range(4):
        pal.fd(50)
        pal.rt(90)
    pal.end_fill()
    pal.pu()
    pal.fd(50)
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

tom.onclick(check, 1)
listen()
done()