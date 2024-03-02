from turtle import Turtle, done

frac = Turtle()
frac.speed(0)
length_long = 500
with open('koch.txt') as file:
    color = file.readline().rstrip()
    n = int(file.readline().rstrip())
frac.color(color)
axiom = 'F'
theorem = 'F-F+F-F'
rule = axiom
for _ in range(n):
    rule = rule.replace(axiom, theorem)
    length_long /= 3
frac.pu()
frac.goto(-250, 150)
frac.pd()
for _ in range(3):
    for item in rule:
        if item == 'F':
            frac.fd(length_long)
        elif item == '-':
            frac.lt(60)
        else:
            frac.rt(120)
    frac.rt(120)

frac.ht()
done()