from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
color = input()
im = Image.new('RGB', (9 * w, 6 * w), 'white')
draw = Draw(im)
draw.ellipse((0, 0, 9 * w, 6 * w), color)
draw.ellipse((5 * w, w, 6.5 * w, 3 * w), 'white')
draw.ellipse((6.5 * w, w, 8 * w, 3 * w), 'white')
draw.ellipse(((6 - 1 / 8) * w, (1.5 - 1 / 8) * w, (6 + 1 / 8) * w, (1.5 + 1 / 8) * w), 'black')
draw.ellipse(((7.5 - 1 / 8) * w, (1.5 - 1 / 8) * w, (7.5 + 1 / 8) * w, (1.5 + 1 / 8) * w), 'black')
im.save('stone.png')
