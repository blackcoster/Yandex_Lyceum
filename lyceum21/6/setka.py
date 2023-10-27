import turtle

mary = turtle.Turtle()
mary.color('purple')
x,y = -280,280
mary.pu()
mary.goto(x,y)
mary.pd()
for i in range(1,10):
    mary.rt(90)
    mary.fd(560)
    mary.pu()
    mary.goto(x+70*i,y)
    mary.pd()
    mary.lt(90)

