import turtle

arch = turtle.Turtle()
arch.color('darkmagenta')
# arch.speed(0)
n = 7
factor = 25
f,s = 1,1
for teta in range(n):
    arch.circle(f*factor,90)
    f,s = s,f+s
f,s = s-f,f
factor2 = 9
for teta in range(n):
    arch.circle(f*factor2,-90)
    f,s = s-f,f
# 8 13
# 5 8
# 3 5

arch.ht()
turtle.done()