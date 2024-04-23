from turtle import Turtle, Screen, done


def left():
    t.seth(180)
    t.fd(10)

def right():
    t.seth(0)
    t.fd(10)

def up():
    t.seth(90)
    t.fd(10)

def down():
    t.seth(-90)
    t.fd(10)

sc = Screen()
t = Turtle('turtle')

sc.onkey(left, 'Left')
sc.onkey(right, 'Right')
sc.onkey(up, 'Up')
sc.onkey(down, 'Down')
sc.listen()
done()