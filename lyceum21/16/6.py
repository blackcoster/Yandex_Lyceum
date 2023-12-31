from turtle import done, Turtle


cube = Turtle()
size = int(input())
c1, c2, c3 = input(), input(), input()
cube.color(c1)
cube.begin_fill()
cube.lt(30)
for _ in range(2):
    cube.fd(size)
    cube.lt(120)
    cube.fd(size)
    cube.lt(60)
cube.end_fill()
cube.color(c2)
cube.begin_fill()
for _ in range(2):
    cube.fd(size)
    cube.rt(120)
    cube.fd(size)
    cube.rt(60)
cube.end_fill()
cube.color(c3)
cube.begin_fill()
cube.lt(120)
for _ in range(2):
    cube.fd(size)
    cube.lt(120)
    cube.fd(size)
    cube.lt(60)
cube.end_fill()
cube.ht()
done()
