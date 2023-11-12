# steps = int(input())
# legs = int(input())
#
# for i in range(steps,0,-1):
#     if (steps-i+1) % legs !=0:
#         print(i,end='_')
#     else:
#         print(i)
#
# # a = 56

# from turtle import Turtle,done
# m = Turtle()
# size = int(input())
# m.color('yellow')
# m.begin_fill()
# for _ in range(5):
#     m.fd(size)
#     m.rt(72)
# m.end_fill()
#
# for _ in range(5):
#     m.color('blue')
#     m.begin_fill()
#     for _ in range(5):
#         m.fd(size)
#         m.lt(72)
#     m.end_fill()
#     m.fd(size)
#     m.rt(72)
# done()


import turtle

length = int(input())
color_cnt = input()
color_out = input()

e = turtle.Turtle()
e.color(color_out)
for i in range(5):
    e.begin_fill()
    for j in range(5):
        e.fd(length)
        e.lt(72)
    e.end_fill()
    e.fd(length)
    e.rt(72)
e.begin_fill()
e.color(color_cnt)
for g in range(5):
    e.fd(length)
    e.rt(72)
e.end_fill()
e.hideturtle()
turtle.done()
