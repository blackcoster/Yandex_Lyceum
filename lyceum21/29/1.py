import turtle

sun = turtle.Turtle()
turtle.tracer(0)
sun.color('navy')
sun.goto(-360, 300)
sun.begin_fill()
for _ in range(2):
    sun.fd(720)
    sun.rt(90)
    sun.fd(600)
    sun.rt(90)
sun.end_fill()
sun.color('yellow')
sun.pu()
sun.goto(0, -120)
sun.seth(0)
sun.pd()
sun.begin_fill()
sun.circle(120)
sun.end_fill()
sun.ht()

tom = turtle.Turtle()
tom.ht()
tom.pu()
tom.color('navy')
tom.goto(240, -120)
tom.pd()

dist = 1

while True:
    tom.clear()
    tom.begin_fill()
    tom.circle(120)
    tom.end_fill()
    turtle.update()
    tom.back(dist)
    if tom.xcor() < -240:
        break

turtle.done()