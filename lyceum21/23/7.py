from turtle import *

p = Turtle()
p.speed(0)
n, size, r, g, b = int(input()), int(input()), int(input()), int(input()), int(input())
colormode(255)
p.pensize(4)
r1, g1, b1 = 255-r, 255-g, 255-b

for i in range(n):
    p.color(r,g,b)
    p.fd(size)
    p.color(r1,g1,b1)
    if n%2==1 and n//2==i:
        p.write(f'dist: {round(p.distance(0,0),1)}',align='center', font=('Arial',14,'normal'))
    elif i<n//2:
        p.write(f'dist: {round(p.distance(0, 0), 1)}', align='left', font=('Arial', 14, 'normal'))
    else:
        p.write(f'dist: {round(p.distance(0, 0), 1)}', align='right', font=('Arial', 14, 'normal'))
    p.lt(360/n)
p.ht()
done()