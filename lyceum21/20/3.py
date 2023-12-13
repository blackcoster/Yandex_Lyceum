# line = input()
# lines = []
# while '!' not in line:
#     lines.append(line)
#     line = input()
# print(lines)
# word = input()
# for i in range(len(lines)):
#     if word in lines[i]:
#         print(i+1, end =' ')

#2
# dishes = []
# line = input()
# while line:
#     dishes.append(line)
#     line = input()
# vegetable = input()
# for item in dishes[::-1]:
#     if 'шпинат' in item or vegetable in item:
#         print(item)

#3

# numbers = [ord('0'), ord('9')]
# letters_up = [ord('A'), ord('Z')]
# letters_down = [ord('a'), ord('z')]
# line = input()
# n, a, p = [], [], []
# for item in line:
#     if numbers[0] <= ord(item) <= numbers[1]:
#         n.append(item)
#     elif letters_up[0] <= ord(item) <= letters_up[1] or \
#             letters_down[0] <= ord(item) <= letters_down[1]:
#         a.append(item)
#     else:
#         p.append(item)
# for item in n:
#     print(item, end='')
# print()
# for item in a:
#     print(item, end='')
# print()
# for item in p:
#     print(item, end='')


#4
# laaaa = []
#
# for i in range(int(input())):
#     laaaa.append(int(input()))
#
# min_value = min(laaaa)
#
# for i in range(len(laaaa)):
#     laaaa[i] = laaaa[i] - min_value
#
# print(laaaa)


#5
# stakan = ...
# nalito = 0
#
# for ora in oranges:
#     if nalito + ora/3 <= stakan:
#         nalito+=ora/3

#6
from turtle import *

point = Turtle()
step, n, k = int(input()), int(input()), int(input())
colors = [input() for _ in range(k)]
size = 2
point.pu()
for i in range(n):
    point.color(colors[i % len(colors)])
    point.fd(size)
    point.dot(20)
    point.lt(36)
    size += step
point.ht()
done()
