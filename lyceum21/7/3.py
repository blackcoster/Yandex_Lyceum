import turtle

mary = turtle.Turtle()
mary.shape('square')
n = 40
size = 1
step = 2
mary.pu()
for i in range(n):
    mary.stamp()
    mary.fd(size + i*step)
    mary.lt(18)
