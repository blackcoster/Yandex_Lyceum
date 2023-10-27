import turtle

hide = turtle.Turtle()
hide.color('rosybrown', 'plum')
hide.pu()
hide.goto(-150, 0)
hide.pd()
hide.hideturtle()

for i in range(3):
    hide.begin_fill()
    hide.lt(60)
    hide.fd(80)
    hide.rt(120)
    hide.fd(80)
    hide.rt(120)
    hide.fd(80)
    hide.rt(180)
    hide.pu()
    hide.fd(100)
    hide.pd()
    hide.end_fill()

hide.showturtle()
turtle.done()