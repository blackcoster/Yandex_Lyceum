from turtle import Turtle, Screen, done, register_shape

N, SIZE = 3, 150
STEP = 1
HALF_WINDOW = N * SIZE // 2


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


def change_circle(obj):
    obj.color('red', 'white')
    obj.shape('circle')
    obj.shapesize(6, outline=6)


def change_cross(obj):
    obj.color('blue', 'white')
    obj.shape('cross')
    obj.shapesize(6, outline=6)


def point(x, y):
    global STEP
    # пересчет экранных координат в координаты вложенного списка
    col = int((x + HALF_WINDOW) // SIZE)
    row = int((y + HALF_WINDOW) // SIZE)
    # в зависимости от того, чей ход
    # записываем значение в board (1 или -1)
    board[row][col] = STEP
    # пересчет координат клетки в списке в координаты окна
    w = col * SIZE + SIZE // 2 - HALF_WINDOW
    h = row * SIZE + SIZE // 2 - HALF_WINDOW
    tom.goto(w, h)
    # вызываем функцию смены формы Черепашки
    if STEP == 1:
        change_cross(tom)
    else:
        change_circle(tom)
    # делаем штамп
    tom.stamp()
    # меняем ход
    STEP = -STEP
    # проверяем выигрыш
    check_result()
    # print(*board, sep='\n')


def check_result():
    res = None
    # проверим, есть ли выигрыш крестиков
    if sum(board[0]) == 3 or sum(board[1]) == 3 or sum(board[2]) == 3 or \
            sum([board[i][0] for i in range(3)]) == 3 or \
            sum([board[i][1] for i in range(3)]) == 3 or \
            sum([board[i][2] for i in range(3)]) == 3 or \
            sum([board[i][i] for i in range(3)]) == 3 or \
            sum([board[3 - i - 1][i] for i in range(3)]) == 3:
        res = 'X'
    elif sum(board[0]) == -3 or sum(board[1]) == -3 or sum(board[2]) == -3 or \
            sum([board[i][0] for i in range(3)]) == -3 or \
            sum([board[i][1] for i in range(3)]) == -3 or \
            sum([board[i][2] for i in range(3)]) == -3 or \
            sum([board[i][i] for i in range(3)]) == -3 or \
            sum([board[3 - i - 1][i] for i in range(3)]) == -3:
        res = '0'
    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        res = '-'
    if res == '-':
        tom.clear()
        tom.goto(0, 0)
        tom.write("It's a Draw", align='center', font=('Comfortaa', 48, 'normal'))
    elif res is not None and res in 'X0':
        tom.clear()
        tom.goto(0, 0)
        tom.write(f"{res} Win!", align='center', font=('Comfortaa', 48, 'normal'))


def start():
    tom.clear()
    tom.goto(0, 0)
    board[:] = [[0] * 3 for _ in range(3)]


sc = Screen()
sc.setup(N * SIZE, N * SIZE, startx=0, starty=0)

board = [[0] * 3 for _ in range(3)]

shape = ((0, 0), (-10, 10), (10, -10),
         (0, 0), (-10, -10), (10, 10))
register_shape('cross', shape)
tom = Turtle()
tom.ht()
tom.pu()
tom.speed(0)

grid()
sc.onclick(point)
sc.onkey(start, 'space')
sc.listen()
done()