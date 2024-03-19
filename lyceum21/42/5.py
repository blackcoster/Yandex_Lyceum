
from PIL import Image
from turtle import Turtle, bgpic, addshape, done

n = int(input())
e = Turtle()
bgpic('shelf.png')
im = Image.open('elephant.gif')
x, y = im.size
shapes = ['elephant.gif']
for i in range(n-1):
    x *= 0.8
    y *= 0.8
    temp_pic = im.resize((int(x), int(y)))
    temp_pic.save(f'elephant{i}.gif')
    shapes.append(f'elephant{i}.gif')
e.pu()
e.goto(-180, 150)
step = 200
for i in range(n):
    addshape(shapes[i])
    e.shape(shapes[i])
    e.stamp()
    e.fd(step)
    step *= 0.8
e.ht()
done()

