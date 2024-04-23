from turtle import Turtle, Screen, done


def one():
    gosha.pensize(1)


def two():
    gosha.pensize(2)


def three():
    gosha.pensize(3)


def four():
    gosha.pensize(4)


def five():
    gosha.pensize(5)


def six():
    gosha.pensize(6)


def seven():
    gosha.pensize(7)


def eight():
    gosha.pensize(8)


def nine():
    gosha.pensize(9)


def red():
    gosha.color('red')


def green():
    gosha.color('green')


def blue():
    gosha.color('blue')


def yellow():
    gosha.color('yellow')


def orange():
    gosha.color('orange')


def up():
    global rad
    rad += 10


def down():
    global rad
    rad -= 10
    if rad < 0:
        rad = 0


def space():
    gosha.circle(rad, 30)


sc = Screen()
gosha = Turtle(shape='turtle')
rad = 100
sc.onkey(up, 'Up')
sc.onkey(down, 'Down')

sc.onkey(one, '1')
sc.onkey(two, '2')
sc.onkey(three, '3')
sc.onkey(four, '4')
sc.onkey(five, '5')
sc.onkey(six, '6')
sc.onkey(seven, '7')
sc.onkey(eight, '8')
sc.onkey(nine, '9')

sc.onkey(red, 'r')
sc.onkey(green, 'g')
sc.onkey(blue, 'b')
sc.onkey(yellow, 'y')
sc.onkey(orange, 'o')

sc.onkey(space, 'space')
sc.listen()

done()
