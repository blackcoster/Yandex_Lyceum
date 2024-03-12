from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
im = Image.new('RGB', (24 * w, 6 * w), 'whitesmoke')
draw = Draw(im)
draw.polygon((0, 0, 5 * w, 3 * w, 0, 6 * w), 'gold')
draw.polygon((0, w, 3.5 * w, 3 * w, 0, 5 * w), 'firebrick')
draw.polygon((5 * w, 3 * w, 7 * w, 2 * w, 9 * w, 3 * w,
              7 * w, 4 * w, 5 * w, 3 * w), outline='navy', width=2)
draw.ellipse((10 * w, 0, 16 * w, 6 * w), 'green', width=2)
draw.ellipse((14 * w, w, 18 * w, 5 * w), outline='darkgreen', width=2)
draw.ellipse((19 * w, 2 * w, 21 * w, 4 * w), 'blue')
draw.line((3.5 * w, 3 * w, 24 * w, 3 * w), 'navy', width=4)
draw.line((23 * w, 2.5 * w, 24 * w, 3 * w, 23 * w, 3.5 * w), 'navy', width=4)
draw.line((13 * w, 0, 13 * w, 6 * w), 'navy', width=2)
im.save('arrow.png')