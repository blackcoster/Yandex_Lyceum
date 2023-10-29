# import turtle
#
# mary = turtle.Turtle()
# n = 500
# mary.speed(6)
# for i in range(0,n,5):
#     mary.fd(i)
#     mary.lt(119)

# import turtle
#
# mary = turtle.Turtle()
# mary.speed(0)
# angle = 360//5
# n = 100
# size = 5
# step = 2
# for i in range(n):
#     mary.fd(size + i*step)
#     mary.lt(angle-3)
# done()


import turtle

mary = turtle.Turtle()
mary.shape('turtle')
tur_size = 0
# mary.shapesize(tur_size)
mary.speed(0)
angle = 360//9 # 9 - количество сторон фигуры
n = 50 #сколько сторон рисовать
size = 2 # начальный размер стороны
step = 3 #шаг
for i in range(n):
    if i % 9 == 0:
        tur_size += 1
    if tur_size > 6:
        tur_size = 6
    mary.shapesize(tur_size)
    mary.fd(size)
    mary.stamp()
    mary.lt(angle-1) #1 - угол на который уменьшаем
    size+=step
mary.done()
