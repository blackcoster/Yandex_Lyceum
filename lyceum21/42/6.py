from PIL import Image
from turtle import setup, done, bgpic

with open('map.txt') as file:
    data = [x.rstrip() for x in file]
    im = Image.new('RGB',(len(data[0]) * 100, len(data) * 100))
    grass = Image.open('grass.png')
    wall = Image.open('wall.png')
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[i][j] == '0':
                im.paste(grass, (i * 100, j * 100))
            else:
                im.paste(wall, (i * 100, j * 100))
    im.save('field.png')

    setup(len(data[0]) * 100, len(data) * 100, 0, 0)
    bgpic('field.png')
    done()


