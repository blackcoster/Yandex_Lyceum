from turtle import Turtle, Screen, done, addshape


def burst(x, y):
    for item in bubbles:
        x0, y0, i = item
        if x0 - 100 <= x <= x0 + 100 and y0 - 100 <= y <= y0 + 100:
            tom.shape('destroyed.gif')
            tom.goto(x0, y0)
            tom.clearstamp(i)
            tom.stamp()
            return


sc = Screen()
sc.setup(startx=0, starty=0)

tom = Turtle()
addshape('bubble.gif')
addshape('destroyed.gif')
tom.pu()
tom.ht()
tom.shape('bubble.gif')
bubbles = []
with open('input.txt') as file:
    for item in file.readlines():
        x, y = map(int, item.rstrip().split())
        tom.goto(x, y)
        i = tom.stamp()
        bubbles.append((x, y, i))

sc.onclick(burst)
sc.listen()
done()