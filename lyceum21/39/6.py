from turtle import Turtle, done


frac = Turtle()
frac.speed(0)
length_long = 600
with open('koch.txt') as file:
    color = file.readline().rstrip()
    n = int(file.readline().rstrip())
frac.color(color)
axiom = 'F'
theorem = 'F-F+F-F'
rule = axiom

for i in range(n):
    rule = rule.replace(axiom,theorem)
    length_long /= 3
    print(rule)
frac.pu()
frac.goto(-300, 0)
frac.pd()
for item in rule:
    if item == 'F':
        frac.fd(length_long)
    elif item == '-':
        frac.lt(60)
    else:
        frac.rt(120)

frac.ht()
done()