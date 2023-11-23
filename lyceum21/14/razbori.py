# Урок Знакомство Ввод и вывод

# Приветствие
print("Привет, Яндекс!")


# Знакомство
print("Привет, Яндекс!")
print("Приятно познакомиться.")

# Имя для Черепашки
print('Как ты хочешь назвать свою Черепашку?')
name = input()
print('Черепашку зовут', name)

# Окно в пикселях
print('В окне Черепашки', 750 * 640, 'пикселей.')

# Двери закрываются
station = input()
print('Осторожно, двери закрываются! Следующая остановка "', station, '"!')

# Путь к файлу
print('C:\\Documents\\', input(), '\\', input())

# Собачка
print("    @")
print("  @@@")
print("@@@ @")
print("@@@@@       @")
print("   @@       @")
print("   @@@@@@@@@@")
print("   @@@@@@@@@")
print("   @@@@@@@@@")
print("   @@@@@@@@@")
print("    @      @")
print("    @      @")
print("    @      @")
print("   @@     @@")

# Фрактальные треугольники
from turtle import *

troy = Turtle()
color = input()
troy.color(color)
troy.lt(60)
troy.fd(200)
troy.rt(120)
troy.fd(100)
troy.rt(120)
troy.fd(100)
troy.lt(120)
troy.fd(100)
troy.lt(120)
troy.fd(100)
troy.rt(120)
troy.fd(100)
troy.rt(120)
troy.fd(200)
done()

# Дополнительные задачи
# Окошко
a = input()
print(a, a, a, a, a, a, a)
print(a, ' ', ' ', a, ' ', ' ', a)
print(a, ' ', ' ', a, ' ', ' ', a)
print(a, a, a, a, a, a, a)
print(a, ' ', ' ', a, ' ', ' ', a)
print(a, ' ', ' ', a, ' ', ' ', a)
print(a, a, a, a, a, a, a)

# Три кота
print(' /\\_/\\      /\\_/\\      /\\_/\\')
print(' (-.-)      (-.o)      (O.O)')
print("""'(")(")'oo '(")(")'oo '(")(")'oo""")

# Конверт
from turtle import *

jack = Turtle()
color = input()
jack.color(color)
jack.lt(30)
jack.fd(240)
jack.rt(120)
jack.fd(120)
jack.rt(120)
jack.fd(240)
jack.rt(150)
jack.fd(208)
jack.lt(150)
jack.fd(120)
jack.lt(60)
jack.fd(120)
jack.lt(60)
jack.fd(120)
jack.lt(90)
jack.fd(208)
done()



# Урок Мини-проект Спирали

# Треугольная спираль
import turtle

triangle = turtle.Turtle()
color = input()
triangle.color(color)
triangle.pu()
triangle.goto(-250, -200)
triangle.pd()
triangle.speed(0)
size, step, n = int(input()), int(input()), int(input())
triangle.lt(60)
for _ in range(n):
    triangle.fd(size)
    triangle.rt(120)
    size -= step

triangle.hideturtle()
turtle.done()

# Многоугольная спираль
import turtle

angle = turtle.Turtle()
color = input()
angle.color(color)
angle.speed(0)
n, size, step = int(input()), int(input()), int(input())

for _ in range(100):
    angle.fd(size)
    angle.lt(360 / n)
    size += step

angle.hideturtle()
turtle.done()

# Пента-спираль
import turtle

penta = turtle.Turtle()
color = input()
penta.color(color)
penta.speed(0)
size, step, alpha = int(input()), int(input()), int(input())
angle = 360 / 5 - alpha
for _ in range(100):
    penta.fd(size)
    penta.lt(angle)
    size += step

penta.hideturtle()
turtle.done()

# Черепаховая спираль
import turtle

tur = turtle.Turtle()
color1, color2 = input(), input()
tur.color(color1, color2)
tur.shape('turtle')
tur_size = 0
tur.speed(0)
n, size, step, m = int(input()), int(input()), int(input()), int(input())
angle = 360 / n - 1
for i in range(m):
    if i % n == 0:
        tur_size += 1
    if tur_size > 6:
        tur_size = 6
    tur.shapesize(tur_size)
    tur.fd(size)
    tur.stamp()
    tur.lt(angle)
    size += step

tur.hideturtle()
turtle.done()


# Урок Проект 1 Графики функций

# Семейство парабол
from turtle import Turtle, done

parabola = Turtle()
parabola.color('rosy brown')
a, b, c, step = float(input()), float(input()), int(input()), int(input())
n = 1
while n <= 5:
    parabola.pu()
    for x in range(-150, 141, 10):
        y = a * x ** 2 + b * x + c
        parabola.goto(x, y)
        parabola.pd()
    c += step
    n += 1

parabola.hideturtle()
done()

# Затухающие колебания
from math import cos, exp
from turtle import Turtle, done

c = Turtle()
c.color(input())
c.pu()
a = a0 = float(input())
c.goto(-350, a)
c.pd()
w = float(input())
t = 1
for x in range(-350, 350):
    y = a * cos(w * x)
    c.goto(x, y)
    a = a0 * exp(-0.005 * t)
    t += 1
c.hideturtle()
done()


# Тюльпан
from turtle import Turtle, done

tulip = Turtle()
flower = input()
line = input()
width = int(input())
tulip.color(flower)
tulip.pu()
tulip.goto(-60, 100)
tulip.pd()
tulip.begin_fill()
for x in range(-60, 60):
    y = -0.0278 * x ** 2 + 200
    tulip.goto(x, y)
for x in range(60, 29, -1):
    y = -0.045 * (x - 45) ** 2 + 110
    tulip.goto(x, y)
for x in range(30, -1, -1):
    y = -0.045 * (x - 15) ** 2 + 110
    tulip.goto(x, y)
for x in range(0, -31, -1):
    y = -0.045 * (x + 15) ** 2 + 110
    tulip.goto(x, y)
for x in range(-30, -61, -1):
    y = -0.045 * (x + 45) ** 2 + 110
    tulip.goto(x, y)
tulip.end_fill()
tulip.pensize(width)
tulip.color(line)
tulip.pu()
tulip.goto(0, 200)
tulip.pd()
for x in range(0, 201):
    y = -0.025 * x ** 2 + 3 * x + 200
    tulip.goto(x, y)
tulip.hideturtle()
done()


# Парусник на волнах
from math import cos
from turtle import Turtle, done

boat = Turtle()
boat.speed(0)
wave = input()
sail = input()
body = input()
boat.color(wave)
boat.pu()
boat.goto(-350, -300)
boat.pd()
boat.begin_fill()
for x in range(-350, 351, 10):
    y = abs(20 * cos(0.025 * x))
    boat.goto(x, y)
boat.goto(350, -300)
boat.goto(-350, -300)
boat.end_fill()

boat.pu()
boat.color(sail)
boat.goto(32, 300)
boat.pd()
boat.begin_fill()
for x in range(32, 137, 10):
    y = -3.15 * x + 400
    boat.goto(x, y)
for x in range(136, -101, -10):
    y = -0.2 * x
    boat.goto(x, y)
for x in range(-100, 33, 10):
    y = 30 * (x + 105) ** 0.5 - 50
    boat.goto(x, y)
boat.end_fill()

boat.pu()
boat.color(body)
boat.goto(-160, 33)
boat.pd()
boat.begin_fill()
for x in range(-160, 221):
    y = 0.0004 * (x - 300) ** 2 + 0.01 * x - 50
    boat.goto(x, y)
for x in range(220, -161, -1):
    y = 0.0025 * (x - 70) ** 2 - 100
    boat.goto(x, y)
boat.end_fill()

boat.hideturtle()
done()


# Необитаемый остров
from math import cos, sin
from turtle import Turtle, done

island = Turtle()
island.speed(0)
sun, waves, land, tree, leaves = input(), input(), input(), input(), input()
island.color(sun)
island.pu()
island.goto(-150, 0)
island.pd()
island.begin_fill()
for x in range(-150, 151, 5):
    y = (150 ** 2 - x ** 2) ** 0.5
    island.goto(x, y)
island.goto(-150, 0)
island.end_fill()

island.color(waves)
island.pu()
island.goto(-350, -300)
island.pd()
island.begin_fill()
for x in range(-350, 351, 5):
    y = 10 * sin(0.144 * x) + 10
    island.goto(x, y)
island.goto(350, -300)
island.goto(-350, -300)
island.end_fill()

island.color(land)
island.pu()
island.goto(-100, -105)
island.pd()
island.begin_fill()
for x in range(-100, 201, 5):
    y = -0.0025 * (x - 50) ** 2 - 50
    island.goto(x, y)
for x in range(200, -101, -5):
    y = 0.0005 * (x - 50) ** 2 - 118
    island.goto(x, y)
island.end_fill()

island.color(tree)
island.pu()
island.goto(-8, 206)
island.pd()
island.begin_fill()
for x in range(-8, 81):
    y = 80 * (80 - x) ** 0.3 - 100
    island.goto(x, y)
for x in range(30, -9, -1):
    y = 50 * (30 - x) ** 0.5 - 100
    island.goto(x, y)
island.end_fill()

island.color(leaves)
island.pu()
island.goto(-40, 138)
island.pd()
island.begin_fill()
for x in range(-40, 21):
    y = 0.002 * (x + 8) ** 3 + 206
    island.goto(x, y)
for x in range(20, -41, -1):
    y = 2.05 * x + 221
    island.goto(x, y)
island.end_fill()

island.pu()
island.goto(-52, 258)
island.pd()
island.begin_fill()
for x in range(-52, -7):
    y = -0.0195 * (x + 60) ** 2 + 260
    island.goto(x, y)
for x in range(-8, -53, -1):
    y = 0.02 * x ** 2 + 205
    island.goto(x, y)
island.end_fill()
island.hideturtle()
done()


# Урок Вложенные циклы
#
# Сколько троек?
n, m = int(input()), int(input())
count = 0
for i in range(n, m + 1):
    while i:
        if i % 10 == 3:
            count += 1
        i //= 10
print(count)


# Количество делителей
n, m = int(input()), int(input())
if n > m:
    n, m = m, n
for i in range(n, m + 1):
    print(f'{i}:\t', end='')
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            print('*', end='')
            if i // j != j:
                print('*', end='')
    print()

# Больше песен
group, average = '', 0
for _ in range(int(input())):
    name = input()
    n = int(input())
    s = 0
    for _ in range(n):
        s += int(input())
    if s / n > average:
        group, average = name, s / n
print(group)


# Примеры
n, m, k = int(input()), int(input()), int(input())
for i in range(n, m + 1, k):
    for j in range(n, m + 1, k):
        print(i, "+", j, "=", i + j, end='\t')
    print()


# Пять делителей
n, m = int(input()), int(input())
if n > m:
    n, m = m, n
for i in range(n, m + 1):
    count = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 1
            if i // j != j:
                count += 1
        if count > 5:
            break
    if count == 5:
        print(i)


# Пятиугольная ромашка
from turtle import *

cam = Turtle()
# cam.speed(0)
size = int(input())
mid, out = input(), input()
cam.color(mid)
cam.begin_fill()
for _ in range(5):
    cam.fd(size)
    cam.rt(72)
cam.end_fill()
for _ in range(5):
    cam.color(out)
    cam.begin_fill()
    for _ in range(5):
        cam.fd(size)
        cam.lt(72)
    cam.end_fill()
    cam.fd(size)
    cam.rt(72)
cam.ht()
done()


# Дополнительные задачи
# Простой заказ
smaller = int(input())
count = int(input())
n = 0
while n < count:
    for i in range(2, int(smaller ** 0.5) + 1):
        if smaller % i == 0:
            break
    else:
        print(smaller)
        n += 1
    smaller += 1


# Змейка по столбцам
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            print(i + 1 + n * j, end='\t')
        else:
            print(n * (j + 1) - i, end='\t')
    print()

# Двухцветное поле
from turtle import *

field = Turtle()
f, s = input(), input()
field.color(s)
field.pu()
field.goto(-280, 280)
field.pd()
field.begin_fill()
for _ in range(4):
    field.fd(560)
    field.rt(90)
field.end_fill()
field.color(f)
for j in range(8):
    for _ in range(4):
        field.begin_fill()
        for i in range(4):
            field.fd(70)
            field.rt(90)
        field.end_fill()
        field.pu()
        field.fd(140)
        field.pd()
    field.pu()
    if j % 2 == 0:
        field.goto(-280 + 70, 280 - (j + 1) * 70)
    else:
        field.goto(-280, 280 - (j + 1) * 70)
    field.pd()
done()