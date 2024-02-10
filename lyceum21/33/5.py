from turtle import Screen, Turtle,done

color, font, size, mode = input(), input(), int(input()),input()
sc = Screen()

sc_params = {'width': 30 * size,
             'height': 6*size,
             'startx': 0,
             'starty':0}
sc.setup(**sc_params)
t = Turtle()
t.color(color)
write_params = {'align':'center',
                'font':(font,size,mode)}

t.write('Привет тебе, о незнакомец!',** write_params)
t.ht()
done()
