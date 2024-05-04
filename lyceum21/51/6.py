from turtle import Turtle, Screen, done

NX, NY, SIZE = 5, 6, 100
DELTA = 100
WORD = []
board = []
RIDDLE, DESCRIPTION = open('input.txt', encoding='utf8').read().rstrip().split(maxsplit=1)
LETTERS = ['ДУМБЗ', 'КЩЮВЙ', 'ЕЖАПЫ', 'ХФШОС', 'ЭГЧИН', 'ЦТРЛЯ']


def grid():
    rows, column = Turtle(), Turtle()
    for item in rows, column:
        item.speed(0)
        item.ht()
        item.pu()
        item.goto(-(NX * SIZE // 2), NY * SIZE // 2 - DELTA // 2)
    column.rt(90)
    for _ in range(NY):
        rows.pd()
        rows.fd(NX * SIZE)
        rows.pu()
        rows.goto(-(NX * SIZE // 2), rows.ycor() - SIZE)
    for _ in range(NX):
        column.goto(column.xcor() + SIZE, NY * SIZE // 2 - DELTA // 2)
        column.pd()
        column.fd(NY * SIZE)
        column.pu()


def letters_arrange():
    let = Turtle()
    let.speed(0)
    let.color('gray')
    let.ht()
    let.pu()
    params = {'align': 'center',
              'font': ('Comfortaa', 68, 'normal')}
    for i in range(NY):
        let.goto(-((NX - 1) * SIZE // 2), (NY - 1 - i * 2) * SIZE // 2 - DELTA)
        col = LETTERS[i]
        board.append(col)
        for j in range(NX):
            let.write(col[j], **params)
            let.fd(SIZE)


def point(x, y):
    tom.clear()
    if y < NY / 2 * SIZE - DELTA / 2:
        i = int((x + NX / 2 * SIZE) / SIZE)
        j = int((-y + NY / 2 * SIZE - DELTA / 2) / SIZE)
        WORD.append(board[j][i])
        tom.goto(0, NY // 2 * SIZE - DELTA // 2)
        params = {'align': 'center',
                  'font': ('Comfortaa', 56, 'normal')}
        tom.write(''.join(WORD), **params)
        check()


def start():
    letters_arrange()
    tom.goto(0, NY // 2 * SIZE - DELTA // 2)
    params = {'align': 'center',
              'font': ('Comfortaa', 26, 'normal')}
    tom.write(DESCRIPTION, **params)


def check():
    if ''.join(WORD) == RIDDLE.upper():
        tom.goto(0, NY // 2 * SIZE + 20)
        tom.color('green')
        params = {'align': 'center',
                  'font': ('Comfortaa', 22, 'normal')}
        text = 'Правильно!'
        tom.write(text, **params)


sc = Screen()
sc.setup(NX * SIZE, NY * SIZE + DELTA, startx=0, starty=0)
# print(sc.window_width(), sc.window_height())
grid()
tom = Turtle()
tom.speed(0)
tom.color('indigo')
tom.ht()
tom.pu()
start()
sc.onclick(point)
done()