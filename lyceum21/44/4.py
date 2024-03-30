import random
from turtle import Turtle, done, addshape, setup, bgpic

setup(800, 800, 0, 0)  # установим размер окна и положение
bgpic('tree.png')
flowers = [Turtle() for _ in range(6)]  # черепашки-цветы
pic_flowers = [f'flower{i}.gif' for i in range(6)]  # картинки для формы
for flower in pic_flowers:  # регистрация форм
    addshape(flower)
places = [(-330, 100), (-250, 250), (0, 350),
          (260, 300), (310, 180), (220, -20)]  # положения цветов и листьев на дереве
for i in range(6):  # размещение цветов и настройка
    flowers[i].ht()
    flowers[i].pu()
    flowers[i].goto(places[i])
    flowers[i].shape(pic_flowers[0])
    flowers[i].st()
for i in range(6):  # анимация цветов
    for flower in flowers:
        flower.shape(pic_flowers[i])

leaves = [Turtle() for _ in range(6)]  # черепашки-листья
pic_leaves = [f'leave{i}.gif' for i in range(5)]  # картинки листьев для форм
for leave in pic_leaves:  # регистрация форм
    addshape(leave)
for i in range(6):  # размещение листьев и настройка
    leaves[i].ht()
    leaves[i].pu()
    leaves[i].goto(places[i])
    leaves[i].shape(pic_leaves[0])
    flowers[i].ht()
    leaves[i].st()
    leaves[i].rt(90)
for i in range(5):  # изменение цвета и длижение листьев
    for leave in leaves:
        leave.shape(pic_leaves[i])
    if i > 2:
        for leave in leaves:
            leave.fd(random.randint(0, 20))
while any([x.ycor() > -500 for x in leaves]):  # падение ниже границы экрана
    for leave in leaves:
        leave.fd(random.randint(0, 20))
done()