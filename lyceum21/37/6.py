from turtle import Turtle, done

filename = input()
with open(filename, encoding='utf8') as in_file:
    name = in_file.readline().rstrip()
    w = int(in_file.readline())
    x, y = [int(a) for a in in_file.readline().rstrip().split()]
    outline, fill = in_file.readline().rstrip().split()
fig = Turtle()
fig.color(outline, fill)
fig.pensize(w // 20)
fig.pu()
fig.goto(x, y)
fig.pd()
fig.begin_fill()
if name == 'Треугольник':
    for _ in range(3):
        fig.fd(w)
        fig.lt(120)
elif name == 'Квадрат':
    for _ in range(4):
        fig.fd(w)
        fig.lt(90)
elif name == 'Круг':
    fig.circle(w)
else:
    for _ in range(6):
        fig.fd(w)
        fig.lt(60)
fig.end_fill()
fig.pu()
fig.goto(0, y - 80)
fig.write(name, align='center', font=('Comfortaa', 36, 'bold'))
fig.ht()
done()