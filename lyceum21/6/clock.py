import turtle

mary = turtle.Turtle()
mary.color('darkgreen')
for i in range(12):
    mary.fd(100)
    mary.rt(30)
    mary.fd(20)
    mary.lt(50)
    mary.fd(40)
    mary.rt(20)
    mary.fd(10)

    mary.pu()
    mary.goto(0,0)
    mary.pd()

    mary.rt(30)