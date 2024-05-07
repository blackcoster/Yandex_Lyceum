from turtle import Screen, Turtle, done, addshape


def func_pu_pd(x, y):
    global CLICK
    CLICK = not CLICK
    if CLICK:
        tom.pu()
    else:
        tom.pd()


CLICK = False
sc = Screen()
sc.setup(startx=0, starty=0)
tom = Turtle()
tom.speed(0)
addshape('brush.gif')
tom.shape('brush.gif')
tom.ondrag(tom.goto)
tom.onclick(func_pu_pd, btn=3)
done()
