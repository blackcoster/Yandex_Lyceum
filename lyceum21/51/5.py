from turtle import Turtle, Screen, done

N, SIZE = 8, 70
HALF_WINDOW = N * SIZE // 2
COLORS = ['aquamarine', 'green']
STEP = 1


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
    draw()


def point(x, y):
    global STEP
    # пересчет экранных координат в координаты вложенного списка
    j = int((x + HALF_WINDOW) // SIZE)
    i = int((y + HALF_WINDOW) // SIZE)
    if not board[j][i]:
        board[j][i] = STEP
        # приведение к середине клетки
        w = ((x + HALF_WINDOW) // SIZE - (N - 1) / 2) * SIZE
        h = ((y + HALF_WINDOW) // SIZE - (N - 1) / 2) * SIZE
        tom.goto(w, h)
        color = board[j][i] if board[j][i] > 0 else 0
        tom.dot(int(0.8 * SIZE), COLORS[color])
        STEP = -STEP


def draw():
    for i in range(8):
        for j in range(8):
            if board[j][i]:
                # пересчет координат клетки в координаты окна
                x = j * SIZE + SIZE // 2 - HALF_WINDOW
                y = i * SIZE + SIZE // 2 - HALF_WINDOW
                tom.goto(x, y)
                color = board[j][i] if board[j][i] > 0 else 0
                tom.dot(int(0.8 * SIZE), COLORS[color])


sc = Screen()
sc.setup(N * SIZE, N * SIZE)

tom = Turtle()
tom.speed(0)
tom.pu()
tom.ht()
sc.onclick(point)
sc.listen()

board = [[0] * 8 for _ in range(8)]
board[4][3] = board[3][4] = 1
board[3][3] = board[4][4] = -1
grid()
done()