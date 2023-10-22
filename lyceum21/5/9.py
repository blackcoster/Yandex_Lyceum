from turtle import *

marfa = Turtle()
marfa.pu()
marfa.goto(0,-200)
marfa.pd()
for i in range(6):
    marfa.fd(200)
    marfa.lt(30)
    if i%2==1:
        marfa.circle(10)
    marfa.lt(30)
done()


