import turtle

triangle = turtle.Turtle()
triangle.color('olivedrab', 'springgreen')
triangle.shapesize(3, 3, outline=4)
n =0
for i in range(5):
    n = triangle.stamp()
    triangle.fd(120)
    triangle.lt(72)
triangle.clearstamp(n)
turtle.done()