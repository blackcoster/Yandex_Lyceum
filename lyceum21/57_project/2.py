from turtle import Screen, Turtle, addshape, done

from PIL import Image


def draw_map():
    for i in range(m):
        for j in range(n):
            ben.goto(-WIDTH // 2 + (j + 0.5) * side, HEIGHT // 2 - (i + 0.5) * side)
            ben.shape(f'image{pic[i][j]}.gif')
            ben.stamp()
    ben.color('white')
    ben.pensize(2)
    for i in range(m - 1):
        ben.goto(-WIDTH // 2, HEIGHT // 2 - side * (i + 1))
        ben.pd()
        ben.goto(WIDTH // 2, HEIGHT // 2 - side * (i + 1))
        ben.pu()
    for i in range(n - 1):
        ben.goto(-WIDTH // 2 + side * (i + 1), HEIGHT // 2)
        ben.pd()
        ben.goto(-WIDTH // 2 + side * (i + 1), -HEIGHT // 2)
        ben.pu()


WIDTH, HEIGHT = 600, 450
n, m = 4, 3
side = WIDTH // n

with open('input.txt') as file:
    filename = file.readline().rstrip()
    pic = [[int(x) for x in line.rstrip().split()]
           for line in file.readlines()]
im = Image.open(filename)
x, y = im.size
for i in range(n):
    for j in range(m):
        im_new = Image.new('RGB', (x // n, y // m))
        im_new.paste(im.crop((i * x // n, j * y // m, (i + 1) * x // n,
                              (j + 1) * y // m)))
        im_new.save(f"image{i * m + j}.gif")

sc = Screen()
sc.setup(startx=0, starty=0)
ben = Turtle()
ben.pu()
ben.ht()
ben.speed(0)
for i in range(n * m):
    addshape(f'image{i}.gif')
draw_map()

done()