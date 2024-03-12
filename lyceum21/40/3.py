from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
im = Image.new('RGB', (12 * w, 14 * w), 'white')
draw = Draw(im)
draw.polygon((2 * w, 0, 6 * w, 3 * w,
              10 * w, 0, 11 * w, 7 * w,
              12 * w, 9 * w, 8 * w, 11 * w,
              4 * w, 11 * w, 0, 9 * w,
              w, 7 * w, 2 * w, 0), fill='#ffa000', outline='black', width=3)
draw.line((2 * w, 0, 3 * w, 3 * w), fill='black', width=3)
draw.line((3 * w, 3 * w, w, 7 * w), fill='black', width=3)
draw.line((3 * w, 3 * w, 6 * w, 3 * w), fill='black', width=3)
draw.line((3 * w, 3 * w, 6 * w, 14 * w), fill='black', width=3)
draw.line((10 * w, 0, 9 * w, 3 * w), fill='black', width=3)
draw.line((9 * w, 3 * w, 6 * w, 14 * w), fill='black', width=3)
draw.line((9 * w, 3 * w, 6 * w, 3 * w), fill='black', width=3)
draw.line((9 * w, 3 * w, 11 * w, 7 * w), fill='black', width=3)
draw.polygon((w, 7 * w, 6 * w, 9 * w,
              11 * w, 7 * w, 6 * w, 14 * w), fill='black', outline='black', width=3)
draw.polygon((w, 7 * w, 4.5 * w, 8.4 * w,
              6 * w, 14 * w), fill='white', outline='black', width=3)
draw.polygon((11 * w, 7 * w, 7.5 * w, 8.4 * w,
              6 * w, 14 * w), fill='white', outline='black', width=3)
im.save('fox.png')