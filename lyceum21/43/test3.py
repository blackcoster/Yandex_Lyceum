# легкий вариант
#
from PIL import Image
im = Image.open('planet.png') # поменять
im = im.convert('RGB') # на всякий случай
x, y = im.size
pixels = im.load()
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = r, min(255, g+20), b
im = im.transpose(1)
im.save('new.png') # поменять


# другие идеи -
# pixels[i, j] = max(0,r - ..), max(0, g - ..), min(255, b + ..)
#
# менять transpose
# FLIP_LEFT_RIGHT = 0 — отразить слева направо; (отн ВЕРТИКАЛИ)
# FLIP_TOP_BOTTOM = 1 — отразить сверху вниз; (ОТН ГОРИЗОНТАЛИ)
# ROTATE_90 = 2 — повернуть на 90 градусов относительно центра против часовой стрелки;
# ROTATE_180 = 3 — повернуть на 180 градусов;
# ROTATE_270 = 4 — повернуть на 270 градусов.
# TRANSPOSE = 5 — транспонировать;
# TRANSVERSE = 6 — транспонировать поперечно.

# обрезка
# im = im.crop((x // 4, y // 4, x // 4 + x // 2, y//4 + y // 2))
# im = im.resize((x,y))

# im = im.crop((0, 0, x // 3, y // 3))
# im = im.resize((x,y))

