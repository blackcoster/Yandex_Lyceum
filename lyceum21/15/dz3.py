from turtle import Turtle, done

tulip = Turtle()
flower = input()
line = input()
width = int(input())
tulip.color(flower)
tulip.pu()
tulip.goto(-60, 100)
tulip.pd()
tulip.begin_fill()
for x in range(-60, 60):
    y = -0.0278 * x ** 2 + 200
    tulip.goto(x, y)
for x in range(60, 29, -1):
    y = -0.045 * (x - 45) ** 2 + 110
    tulip.goto(x, y)
for x in range(30, -1, -1):
    y = -0.045 * (x - 15) ** 2 + 110
    tulip.goto(x, y)
for x in range(0, -31, -1):
    y = -0.045 * (x + 15) ** 2 + 110
    tulip.goto(x, y)
for x in range(-30, -61, -1):
    y = -0.045 * (x + 45) ** 2 + 110
    tulip.goto(x, y)
tulip.end_fill()
tulip.pensize(width)
tulip.color(line)
tulip.goto(0, 200)
tulip.pd()
for x in range(0, 201):
    y = -0.025 * x ** 2 + 3 * x + 200
    tulip.goto(x, y)
tulip.hideturtle()
done()
