from turtle import *

marfa = Turtle()
marfa.pu()
marfa.goto(0,-200)
marfa.pd()
for i in range(6):
    marfa.lt(60)
    marfa.fd(200)
    marfa.dot(8,'red')
done()


