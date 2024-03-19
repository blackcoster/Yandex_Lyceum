# Солнышко
from turtle import Turtle, done, bgpic

color = input()
n = int(input())
bgpic('sky.png')
sun = Turtle()
sun.speed(0)
size = step = 1
sun.color(color)
for i in range(n):
    sun.pensize(size)
    sun.fd(size + i * step)
    sun.lt(30)
    size += 1
sun.ht()
done()


# Пазл
from turtle import Screen, done

from PIL import Image

im = Image.open('castle.png')
x, y = im.size
images = [im.crop((j * x // 3, i * y // 3,
                   (j + 1) * x // 3, (i + 1) * y // 3))
          for i in range(3) for j in range(3)]
im_new = Image.new('RGB', im.size)
with open('puzzle.txt') as file:
    data = [int(line) for line in file]
for i, n in enumerate(data):
    im_new.paste(images[i], (n % 3 * x // 3, n // 3 * y // 3))
im_new.save('fon.png')
sc = Screen()
sc.bgpic('fon.png')
done()


# Дерево модерн
from turtle import Turtle, done

bgpic('fon.png')
frac = Turtle()
size = 10
length = 200
x, y = [int(a) for a in input().split()]
n = int(input())
frac.speed(0)
frac.color('maroon')
frac.pensize(size)
frac.pu()
frac.goto(x, y)
frac.lt(90)
frac.pd()
# 0 итерация
frac.fd(length)
points = [{'xy': frac.pos(), 'angle': frac.heading()}]
# 1 итерация
for _ in range(n):
    size -= 1
    length //= 2
    points1 = []
    for item in points:
        frac.pensize(size)
        for angle in -45, 45:
            frac.pu()
            frac.goto(item['xy'])
            frac.pd()
            frac.seth(item['angle'] + angle)
            frac.fd(length)
            points1 += [{'xy': frac.pos(), 'angle': frac.heading()}]
    points = points1.copy()
frac.ht()
done()