from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
colors = [int(x) for x in input().split()]
coords = [int(x) for x in input().split()]

im = Image.new('RGB', (900, 600), 'white')
draw = Draw(im)
j = 0
for i in range(len(colors)):
    x, y = coords[j:j + 2]
    j += 2
    draw.ellipse((x, y, x + 9 * w, y + 6 * w), (colors[i],) * 3)
    draw.ellipse((x + 5 * w, y + w, x + 6.5 * w, y + 3 * w), 'white')
    draw.ellipse((x + 6.5 * w, y + w, x + 8 * w, y + 3 * w), 'white')
    draw.ellipse((x + (6 - 1 / 8) * w, y + (1.5 - 1 / 8) * w, x + (6 + 1 / 8) * w, y + (1.5 + 1 / 8) * w), 'black')
    draw.ellipse((x + (7.5 - 1 / 8) * w, y + (1.5 - 1 / 8) * w, x + (7.5 + 1 / 8) * w, y + (1.5 + 1 / 8) * w), 'black')
im.save('stones.png')