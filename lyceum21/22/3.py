from turtle import *

t = Turtle()
t.speed(0)
t.pu()
t.goto(-320, -150)
colormode(255)
t.pen(pensize=10, pencolor=(65, 105, 225), pendown=True)
t.fd(640)
t.lt(90)
t.fd(320)
t.lt(90)
t.fd(640)
t.lt(90)
t.fd(320)
t.lt(90)

t.pu()
t.color(0, 0, 0)
t.goto(0, -30)
t.pd()
small_psi = '\N{Greek Small Letter Psi}'
big_psi = '\N{Greek Capital Letter Psi}'
integral = '\u222B'
skobka = '\u232A'
text = f'|{small_psi}(t){skobka}={integral}{big_psi}(x, t)|x{skobka}dx'
t.write(text, font=('Times New Roman', 60, 'normal'), align='center')
t.ht()
done()

