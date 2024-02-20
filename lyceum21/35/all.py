from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
fig.color(colors[i])
points = []
fig.begin_fill()
for _ in range(4):
    fig.fd(100)
    points.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[i % 2]})
    i += 1
    points.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[i % 2]})
    i += 1
    fig.lt(90)
fig.end_fill()
points1 = []
i = 0
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(4):
        fig.fd(100)
        if fig.pos() != item['xy']:
            i += 1
        if i % 8 == 1:
            points1.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[i % 2]})
        elif i % 8 == 2:
            points1.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[i % 2]})
            points1.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[(i + 1) % 2]})
        elif i % 8 == 3:
            points1.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[(i + 1) % 2]})
        fig.lt(90)
    fig.end_fill()
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(4):
        fig.fd(100)
        fig.lt(90)
    fig.end_fill()
fig.ht()
done()





#2
from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
points = []
i = 0
fig.color(colors[i])
fig.begin_fill()
for _ in range(3):
    fig.fd(100)
    for k in -2, -1, 0, 1:
        points.append({'xy': fig.pos(),
                       'angle': fig.heading() + k * 60,
                       'color': colors[i % 2]})
        i += 1
    fig.lt(120)
fig.end_fill()
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(3):
        fig.fd(100)
        fig.lt(120)
    fig.end_fill()
fig.ht()
done()






#3
from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
points = []
i = 0
fig.color(colors[i])
fig.begin_fill()
for _ in range(3):
    fig.fd(100)
    for k in -2, -1, 0, 1:
        points.append({'xy': fig.pos(),
                       'angle': fig.heading() + k * 60,
                       'color': colors[i % 2]})
        i += 1
    fig.lt(120)
fig.end_fill()
points1 = []
i = 0
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(3):
        i += 1
        fig.fd(100)
        if i % 12 == 4:
            for k in -2, -1, 0, 1:
                points1.append({'xy': fig.pos(),
                                'angle': fig.heading() + k * 60,
                                'color': colors[(k + 1) % 2]})
        elif i % 6 == 1:
            for k in -1, 0:
                points1.append({'xy': fig.pos(),
                                'angle': fig.heading() + k * 60,
                                'color': colors[k % 2]})
        fig.lt(120)
    fig.end_fill()
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(3):
        fig.fd(100)
        fig.lt(120)
    fig.end_fill()
fig.ht()
done()




#4

from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
points = []
fig.color(colors[i])
fig.begin_fill()
for _ in range(6):
    fig.fd(50)
    i += 1
    points.append({'xy': fig.pos(),
                   'angle': fig.heading() - 60,
                   'color': colors[1:][i % 2]})
    fig.lt(60)
fig.end_fill()
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        fig.lt(60)
    fig.end_fill()
fig.ht()
done()



#5
from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
points = []
fig.color(colors[i])
fig.begin_fill()
for _ in range(6):
    fig.fd(50)
    i += 1
    points.append({'xy': fig.pos(),
                   'angle': fig.heading() - 60,
                   'color': colors[1:][i % 2]})
    fig.lt(60)
fig.end_fill()
i = 0
points1 = []
colors1 = [colors[2], colors[0], colors[1], colors[0]]
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        i += 1
        if i % 6 in (1, 2):
            points1.append({'xy': fig.pos(),
                            'angle': fig.heading() - 60,
                            'color': colors1[i % 4]})

        fig.lt(60)
    fig.end_fill()
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        fig.lt(60)
    fig.end_fill()
fig.ht()
done()



#6
from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
points = []
fig.color(colors[i])
fig.begin_fill()
for _ in range(6):
    fig.fd(50)
    i += 1
    points.append({'xy': fig.pos(),
                   'angle': fig.heading() - 60,
                   'color': colors[1:][i % 2]})
    fig.lt(60)
fig.end_fill()
i = 0
points1 = []
colors1 = [colors[2], colors[0], colors[1], colors[0]]
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        i += 1
        if i % 6 in (1, 2):
            points1.append({'xy': fig.pos(),
                            'angle': fig.heading() - 60,
                            'color': colors1[i % 4]})
        fig.lt(60)
    fig.end_fill()
points2 = []
colors2 = ['royalblue', 'steelblue', 'royalblue', 'blueviolet', 'steelblue', 'blueviolet']
i = k = 0
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        i += 1
        if i % 12 in (7, 8, 9):
            points2.append({'xy': fig.pos(),
                            'angle': fig.heading() - 60,
                            'color': colors2[k % 6]})
            k += 1
        fig.lt(60)
    fig.end_fill()
for item in points2:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(6):
        fig.fd(50)
        fig.lt(60)
    fig.end_fill()
fig.ht()
done()




# ladno vot vam dop zadachi

from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
fig.color(colors[i])
points = []
fig.begin_fill()
for _ in range(6):
    fig.fd(50)
    # для квадрата
    points.append({'xy': fig.pos(),
                   'angle': fig.heading() - 180,
                   'color': colors[1:][i % 2]})
    i += 1
    # для треугольника
    points.append({'xy': fig.pos(),
                   'angle': fig.heading() - 90,
                   'color': colors[1:][i % 2]})
    i += 1
    fig.lt(60)
fig.end_fill()
points1 = []
k = 0
for i in range(len(points)):
    item = points[i]
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    if i % 2:
        for _ in range(2):
            fig.fd(50)
            fig.lt(120)
        # для шестиугольника
        points1.append({'xy': fig.pos(),
                        'angle': fig.heading() + 150,
                        'color': colors[:2][(i + 1) % 2]})
        fig.fd(50)
        fig.lt(120)

    else:
        for _ in range(3):
            fig.fd(50)
            fig.lt(90)
        # для квадрата
        points1.append({'xy': fig.pos(),
                        'angle': fig.heading() - 150,
                        'color': colors[:2][(i + 1) % 2]})
        fig.fd(50)
        fig.lt(90)

    fig.end_fill()
for i in range(len(points1)):
    item = points1[i]
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    if i % 2 == 0:
        for _ in range(4):
            fig.fd(50)
            fig.lt(90)
    else:
        for _ in range(6):
            fig.fd(50)
            fig.lt(60)
    fig.end_fill()
fig.ht()
done()








from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
points = []
i = 0
fig.color(colors[i])
fig.begin_fill()
for _ in range(3):
    fig.rt(90)
    fig.circle(20, 180)
    fig.circle(-20, 180)
    fig.lt(90)
    for k in -2, -1, 0, 1:
        points.append({'xy': fig.pos(),
                       'angle': fig.heading() + k * 60,
                       'color': colors[i % 2]})
        i += 1
    fig.lt(120)
fig.end_fill()
points1 = []
i = 0
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(3):
        i += 1
        fig.rt(90)
        fig.circle(20, 180)
        fig.circle(-20, 180)
        fig.lt(90)
        if i % 12 == 4:
            for k in -2, -1, 0, 1:
                points1.append({'xy': fig.pos(),
                                'angle': fig.heading() + k * 60,
                                'color': colors[(k + 1) % 2]})
        elif i % 6 == 1:
            for k in -1, 0:
                points1.append({'xy': fig.pos(),
                                'angle': fig.heading() + k * 60,
                                'color': colors[k % 2]})
        fig.lt(120)
    fig.end_fill()
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(3):
        fig.rt(90)
        fig.circle(20, 180)
        fig.circle(-20, 180)
        fig.lt(90)
        fig.lt(120)
    fig.end_fill()
fig.ht()
done()









from turtle import Turtle, done

fig = Turtle()
fig.speed(0)
colors = input().split()
i = 0
fig.color(colors[i])
points = []
fig.begin_fill()
for _ in range(4):
    fig.rt(90)
    fig.circle(20, 180)
    fig.circle(-20, 180)
    fig.lt(90)
    points.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[i % 2]})
    i += 1
    points.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[i % 2]})
    i += 1
    fig.lt(90)
fig.end_fill()
points1 = []
i = 0
for item in points:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(4):
        fig.rt(90)
        fig.circle(20, 180)
        fig.circle(-20, 180)
        fig.lt(90)
        if fig.pos() != item['xy']:
            i += 1
        if i % 8 == 1:
            points1.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[i % 2]})
        elif i % 8 == 2:
            points1.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[i % 2]})
            points1.append({'xy': fig.pos(), 'angle': fig.heading(), 'color': colors[(i + 1) % 2]})
        elif i % 8 == 3:
            points1.append({'xy': fig.pos(), 'angle': fig.heading() - 90, 'color': colors[(i + 1) % 2]})
        fig.lt(90)
    fig.end_fill()
for item in points1:
    fig.pu()
    fig.goto(item['xy'])
    fig.seth(item['angle'])
    fig.color(item['color'])
    fig.pd()
    fig.begin_fill()
    for _ in range(4):
        fig.rt(90)
        fig.circle(20, 180)
        fig.circle(-20, 180)
        fig.lt(90)
        fig.lt(90)
    fig.end_fill()
fig.ht()
done()