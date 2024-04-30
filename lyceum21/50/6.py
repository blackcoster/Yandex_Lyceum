from turtle import Turtle, done, bgcolor, ontimer, bgpic


def day():
    window.clear()
    window.pu()
    window.goto(-165, -75)
    window.pd()
    bgcolor('cornflowerblue')
    window.color('white')
    window.begin_fill()
    for _ in range(4):
        window.fd(100)
        window.rt(90)
    window.end_fill()


def night():
    window.clear()
    window.pu()
    window.goto(-165, -75)
    window.pd()
    bgcolor('navy')
    window.color('yellow')
    window.begin_fill()
    for _ in range(4):
        window.fd(100)
        window.rt(90)
    window.end_fill()


bgpic('house.png')
window = Turtle()
window.speed(0)
window.ht()
day()

for i in range(5):
    if i % 2:
        ontimer(day, 1000 * (i + 1))
    else:
        ontimer(night, 1000 * (i + 1))

done()