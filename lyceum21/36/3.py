from turtle import Turtle, done

frac = Turtle()
colors = input().split()
frac.color(colors[0])
frac.speed(0)
x0, y0 = -300, 300
length = 600

# 0 iteration
frac.pu()
frac.goto(x0, y0)
frac.pd()
frac.begin_fill()
for _ in range(4):
    frac.fd(length)
    frac.rt(90)
frac.end_fill()
n = 2
frac.color(colors[-1])
x_list = [x0, x0 + length / 3, x0 + 2 * length / 3]
y_list = [y0, y0 - length / 3, y0 - 2 * length / 3]
temp = [(i, j) for i in x_list for j in y_list]
squares = [temp.pop(len(temp) // 2)]
new_squares = temp.copy()
squares_iteration = []
for _ in range(n):
    length /= 3
    for item in squares:
        frac.pu()
        frac.goto(item)
        frac.pd()
        frac.begin_fill()
        for _ in range(4):
            frac.fd(length)
            frac.rt(90)
        frac.end_fill()
    squares = []
    for item in new_squares:
        x0, y0 = item
        x_list = [x0, x0 + length / 3, x0 + 2 * length / 3]
        y_list = [y0, y0 - length / 3, y0 - 2 * length / 3]
        temp = [(i, j) for i in x_list for j in y_list]
        squares.append(temp.pop(len(temp) // 2))
        squares_iteration.extend(temp)
    new_squares = squares_iteration.copy()
    squares_iteration.clear()

frac.ht()
done()
