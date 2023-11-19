import turtle

arch = turtle.Turtle()
arch.color('darkmagenta')
arch.speed(0)
n = 7
factor = 20
f,s = 1,1
for teta in range(n):
    arch.circle(f*factor,90)
    f,s = s,f+s
arch.ht()
turtle.done()