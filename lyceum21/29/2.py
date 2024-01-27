from turtle import Turtle, tracer, done, update

wall = Turtle()
tracer(0)
wall.color('maroon')
wall.pensize(3)
wall.pu()
wall.goto(-350, 300)
wall.pd()
for x, y in (-350, -300), (350, -300), (350, 300):
    wall.goto(x, y)
wall.ht()

ball = Turtle()
ball.shape('circle')
ball.color('blueviolet')
ball.turtlesize(2)
ball.goto(-340, 200)


vel_x = 1
vel_y = 0
acc = -0.1

while True:
    ball.clear()
    ball.goto(ball.xcor() + vel_x, ball.ycor() + vel_y)
    vel_y += acc
    update()
    if ball.ycor() < -290:
        vel_y *= -1
    if ball.xcor() > 340 or ball.xcor() < -340:
        vel_x *= -1

done()