from turtle import Turtle, addshape, done

berry = Turtle()
addshape('berry.gif')
berry.shape('berry.gif')
berry.pu()

line = input()
while line:
    x, y = [int(x) for x in line.split()]
    berry.goto(x, y)
    berry.stamp()
    line = input()
done()