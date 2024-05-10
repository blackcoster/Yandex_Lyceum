# numbers = list(map(int, input().split()))
# res = sum(filter(lambda num: min(numbers) < num < max(numbers), numbers))
# print(res)

# import sys
# for line in sys.stdin:
#     if all(['a' in x for x in line.split()]):
#         print(' '.join(line.split()))
#         break

# import sys
# for line in sys.stdin:
#     if any(['A' in x for x in line.split()]):
#         print(' '.join(line.split()))


# import sys
# words = []
# for line in sys.stdin:
#     words.extend(line.rstrip().split())
# res = sorted(set(words), key=lambda x: (words.count(x), x), reverse=True)
# print(*res,sep='\n')

# import sys
# res = []
# for item in sys.stdin:
#     ids, *rest = map(int, item.split())
#     res.append((sum(rest)/len(rest),(len(rest)),ids))
# temp = sorted(res, key = lambda x:(-x[0],-x[1]))
# print(temp[0][-1],temp[0][0])


from turtle import Turtle, Screen, done


def func_letter(letter):
    global LETTER
    LETTER = letter


def func_write(x, y):
    global LETTER
    if LETTER:
        tom.goto(x, y)
        tom.write(LETTER.upper(), align='center', font=(
            'Roboto', 48, 'bold'
        ))
        LETTER = ''


LETTER = ''
sc = Screen()
sc.setup(startx=0, starty=0)

tom = Turtle()
tom.color('crimson')
tom.pu()
tom.ht()

sc.onclick(func_write)
sc.onkeypress(lambda: func_letter('a'), 'a')
sc.onkeypress(lambda: func_letter('b'), 'b')
sc.onkeypress(lambda: func_letter('c'), 'c')
sc.onkeypress(lambda: func_letter('d'), 'd')
sc.onkeypress(lambda: func_letter('e'), 'e')
sc.onkeypress(lambda: func_letter('f'), 'f')
sc.onkeypress(lambda: func_letter('g'), 'g')
sc.onkeypress(lambda: func_letter('h'), 'h')
sc.onkeypress(lambda: func_letter('i'), 'i')
sc.onkeypress(lambda: func_letter('j'), 'j')
sc.onkeypress(lambda: func_letter('k'), 'k')
sc.onkeypress(lambda: func_letter('l'), 'l')
sc.onkeypress(lambda: func_letter('m'), 'm')
sc.onkeypress(lambda: func_letter('n'), 'n')
sc.onkeypress(lambda: func_letter('o'), 'o')
sc.onkeypress(lambda: func_letter('p'), 'p')
sc.onkeypress(lambda: func_letter('q'), 'q')
sc.onkeypress(lambda: func_letter('r'), 'r')
sc.onkeypress(lambda: func_letter('s'), 's')
sc.onkeypress(lambda: func_letter('t'), 't')
sc.onkeypress(lambda: func_letter('u'), 'u')
sc.onkeypress(lambda: func_letter('v'), 'v')
sc.onkeypress(lambda: func_letter('w'), 'w')
sc.onkeypress(lambda: func_letter('x'), 'x')
sc.onkeypress(lambda: func_letter('y'), 'y')
sc.onkeypress(lambda: func_letter('z'), 'z')
sc.listen()
done()
