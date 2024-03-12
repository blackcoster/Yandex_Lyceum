from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
im = Image.new('RGB', (18 * w, 19 * w), 'white')
draw = Draw(im)
draw.polygon((0, w, 14 * w, 8 * w,
              14 * w, 10 * w, 2 * w, 4 * w,
              2 * w, 19 * w, 0, 18 * w), 'ghostwhite',
             outline='dimgray', width=2)
draw.polygon((0, w, 2 * w, 0,
              18 * w, 8 * w, 4 * w, 16 * w,
              3 * w, 14 * w, 14 * w, 8 * w), 'gainsboro',
             outline='dimgray', width=2)
draw.polygon((2 * w, 4 * w, 4 * w, 5 * w,
              4 * w, 16 * w, 18 * w, 8 * w,
              18 * w, 10 * w, 2 * w, 19 * w), 'darkgray',
             outline='dimgray', width=2)

im.save('triangle.png')