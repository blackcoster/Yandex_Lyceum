from PIL import Image
#
# images = [Image.open(f'feet/bird{i}.png') for i in range(8)]
#
# images[0].save('feet/bird.gif',
#                save_all=True,  # сохранить все
#                append_images=images[1:],  # добавление изображений
#                optimize=True,
#                duration=100,  # продолжительность анимации в мс
#                loop=0)  # зацикливание



# NOT DZ !!!!!!

from PIL import Image

for i in range(8):
    im = Image.open(f'feet/bird{i}.png')
    x, y = im.size
    im = im.resize((x // 2, y // 2))
    im.save(f'new/bird{i}.gif')

from turtle import *

bgpic('road.png')
bird = Turtle()
bird.pu()
bird.goto(-300, -200)
images = [f'new/bird{i}.gif' for i in range(8)]
for i in range(8):
    addshape(images[i])
for i in range(50):
    bird.shape(images[i % 8])
    bird.fd(12)
done()