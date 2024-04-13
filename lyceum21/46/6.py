from turtle import Turtle, done, textinput

t = Turtle()
t.speed(0)
col = textinput('Выбор цвета', 'Введите строку - название цвета звезды')
if col is None:
    col = 'black'
t.color(col)
t.pensize(3)

side = 200
delta = 10

for i in range(120):
    t.fd(side)
    t.back(side)
    t.lt(3)
    ost = i % 20
    if 0 <= ost <= 9:
        side += delta
    else:
        side -= delta
done()
