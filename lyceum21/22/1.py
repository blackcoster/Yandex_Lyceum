from turtle import *
t = Turtle()
t.speed(0)
h = int(input())
r,g,b = int(input()),int(input()),int(input())
size = int(input())
colormode(255)
for _ in range(5):
    t.pu()
    t.goto(-h,-h//2)
    t.pd()
    t.color(r,g,b)
    t.begin_fill()
    for _ in range(2):
        t.fd(2*h)
        t.lt(90)
        t.fd(h)
        t.lt(90)
    t.end_fill()
    h = h - h/10
    r-=10
    g-=10
    b-=10

t.color(255,255,255)
t.pu()
t.goto(0,-0.5*size)
t.pd()
t.write('ВЫХОД',align='center',font=('Arial',size,'bold'))
t.ht()
done()


