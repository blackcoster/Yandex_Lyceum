import turtle

philip = turtle.Turtle()
for i in range(6):
    if i % 3 == 0:
        philip.color("yellowgreen")
    elif i % 3 == 1:
        philip.color("orchid")
    else:
        philip.color("yellow")
    philip.begin_fill()
    philip.lt(35)
    philip.fd(100)
    philip.lt(90)
    philip.fd(100)
    philip.lt(90)
    philip.fd(100)
    philip.lt(90)
    philip.fd(100)
    philip.lt(90)
    philip.end_fill()
turtle.done()