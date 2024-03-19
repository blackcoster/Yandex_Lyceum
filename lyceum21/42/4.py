import turtle

fur = turtle.Turtle()
turtle.bgpic('fon.png')
turtle.addshape('fur.gif')
fur.shape('fur.gif')
fur.pu()
fur.goto(-300, 150)
fur.stamp()
n = int(input()) - 1
for _ in range(n):
    fur.circle(-700, 15)
    fur.stamp()
turtle.done()