import turtle

brown = turtle.Turtle()
brown.color('sandybrown', 'peru')
brown.shape('turtle')
brown.shapesize(3, outline=3)
brown.pu()
brown.goto(-250, 0)
for i in range(4):
    brown.stamp()
    brown.fd(100 + i * 20)
turtle.done()