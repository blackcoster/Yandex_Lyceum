import turtle

t = turtle.Turtle()
t.color('teal')
n = 20
while n > 0:
    t.pensize(n)
    t.fd(20)
    n -= 4
turtle.done()

