from turtle import Turtle, done

filename = input()
with open(filename, encoding='utf8') as in_file:
    colors = in_file.readline().rstrip().split()
    w = int(in_file.readline())
    lines = [line.rstrip() for line in in_file.readlines()]
n, m = len(lines), len(lines[0])
width = m * w
height = n * w
x0, y0 = -(width / 2), height / 2 - w
fig = Turtle()
fig.speed(0)
k = 0
for i in range(n):
    fig.pu()
    fig.goto(x0, y0)
    fig.pd()
    for j in range(m):
        fig.color(colors[k % len(colors)])
        fig.begin_fill()
        if lines[i][j] == 'T':
            for _ in range(3):
                fig.fd(w)
                fig.lt(120)
            fig.fd(w)
        elif lines[i][j] == 'S':
            for _ in range(4):
                fig.fd(w)
                fig.lt(90)
            fig.fd(w)
        else:
            fig.pu()
            fig.fd(w / 2)
            fig.pd()
            fig.circle(w / 2)
            fig.pu()
            fig.fd(w / 2)
            fig.pd()
        fig.end_fill()
        k += 1
    y0 -= w

fig.ht()
done()