from turtle import *

marfa = Turtle()
marfa.pu()
marfa.goto(0,-200)
marfa.pd()
for i in range(250,51,-50):
    marfa.circle(i)
done()