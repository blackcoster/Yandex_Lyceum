from turtle import bgpic, Turtle, addshape, done
from PIL import Image

w, h = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]
bgpic('fon.png')
t = Turtle()
Image.open('house.gif').resize((w, h)).save('temp.gif')
addshape('temp.gif')
t.pu()
t.goto(x, y)
t.shape('temp.gif')
t.stamp()
done()
