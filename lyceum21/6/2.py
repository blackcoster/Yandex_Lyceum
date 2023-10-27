import turtle

philip = turtle.Turtle()
philip.rt(180)
for i in range(12):
    if i % 4 == 0:
        philip.color("lawngreen")
        philip.pencolor('teal')
    elif i % 4 == 1:
        philip.color("navy", "dodgerblue")
    elif i % 4 == 2:
        philip.color("firebrick", "deeppink")
    else:
        philip.color("saddlebrown", "gold")
    philip.begin_fill()
    philip.circle(50)
    philip.pu()
    philip.rt(30)
    philip.fd(40)
    philip.pd()
    philip.end_fill()
turtle.done()