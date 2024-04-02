from PIL import Image
from PIL.ImageDraw import ImageDraw

side = int(input())
diameter = int(input())
r, g, b = [int(x) for x in input().split()]
step = int(input())

im = Image.new('RGB', (side, side), 'white')
draw = ImageDraw(im)
for i in range(side // diameter):
    for j in range(side // diameter):
        draw.ellipse((i * diameter, j * diameter, (i + 1) * diameter, (j + 1) * diameter),
                     fill=(r + step * i, g, b + step * j))
im.save('bubbles.png')
