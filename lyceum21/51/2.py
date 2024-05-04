from turtle import Turtle, Screen, done

N, SIZE = 7, 80
HALF_WINDOW = N * SIZE // 2
COLORS = ['gold', 'orange', 'orangered', 'crimson']


def grid():
    row, column = Turtle(), Turtle()
    for item in row, column:
        item.speed(0)
        item.ht()
        item.pu()
        item.goto(-(N * SIZE // 2), N * SIZE // 2)
    column.rt(90)
    for _ in range(N):
        row.goto(-(N * SIZE // 2), row.ycor() - SIZE)
        column.goto(column.xcor() + SIZE, N * SIZE // 2)
        for item in row, column:
            item.pd()
            item.fd(N * SIZE)
            item.pu()


def point(x, y):
    # приведение к середине клетки
    w = ((x + HALF_WINDOW) // SIZE - (N - 1) / 2) * SIZE
    h = ((y + HALF_WINDOW) // SIZE - (N - 1) / 2) * SIZE
    tom.goto(w, h)
    if (w, h) in board:
        board[(w, h)] = (board[(w, h)] + 1) % 4
    else:
        board[(w, h)] = 0
    tom.dot(int(0.8 * SIZE), COLORS[board[(w, h)]])


sc = Screen()
sc.setup(N * SIZE, N * SIZE)
grid()
tom = Turtle()
tom.speed(0)
tom.pu()
tom.ht()
sc.onclick(point)
sc.listen()

board = {}
done()