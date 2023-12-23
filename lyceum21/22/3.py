# from turtle import *
#
# t = Turtle()
# t.speed(0)
# t.pu()
# t.goto(-320, -150)
# colormode(255)
# t.pen(pensize=10, pencolor=(65, 105, 225), pendown=True)
# t.fd(640)
# t.lt(90)
# t.fd(320)
# t.lt(90)
# t.fd(640)
# t.lt(90)
# t.fd(320)
# t.lt(90)
#
# t.pu()
# t.color(0, 0, 0)
# t.goto(0, -30)
# t.pd()
# small_psi = '\N{Greek Small Letter Psi}'
# big_psi = '\N{Greek Capital Letter Psi}'
# integral = '\u222B'
# skobka = '\u232A'
# text = f'|{small_psi}(t){skobka}={integral}{big_psi}(x, t)|x{skobka}dx'
# t.write(text, font=('Times New Roman', 60, 'normal'), align='center')
# t.ht()
# done()


from turtle import *
p = Turtle()
p.speed(5)
dlina = 640
shirina = 300
text = input()
shrift = int(input())
r, g, b = int(input()), int(input()), int(input())
colormode(255)
for _ in range(6):
    p.penup()
    p.goto(-dlina, -shirina)
    p.pendown()
    p.color(r, g, b)
    p.begin_fill()
    for _ in range(2):
        p.fd(dlina)
        p.lt(90)
        p.fd(shirina)
        p.lt(90)
    p.end_fill()
    dlina -= 20
    shirina -= 20
    r += 15
    g += 15
    b += 15
p.color(r - (15 * 6), g - (15 * 6), b - (15 * 6))
p.penup()
p.goto(0, -shrift * 0.8)
p.pendown()
p.write(text, font=('Droid Sans', shrift, 'normal'), align='center')
p.hideturtle()
done()