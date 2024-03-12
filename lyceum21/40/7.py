from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
nose = input()
im = Image.new('RGB', (12 * w, 13 * w), 'white')
draw = Draw(im)
draw.pieslice(((0, 11 * w), (4 * w, 15 * w)), 180, 0, 'darkgray',
              outline='dimgray', width=3)
draw.pieslice(((8 * w, 11 * w), (12 * w, 15 * w)), 180, 0, 'darkgray',
              outline='dimgray', width=3)
draw.polygon((3 * w, 0, 5 * w, 3 * w,
              7 * w, 3 * w, 9 * w, 0,
              10 * w, 13 * w, 2 * w, 13 * w), 'darkgray',
             outline='dimgray', width=3)
draw.pieslice(((4 * w, 12 * w), (6 * w, 14 * w)), 180, 0, 'darkgray',
              outline='dimgray', width=3)
draw.pieslice(((6 * w, 12 * w), (8 * w, 14 * w)), 180, 0, 'darkgray',
              outline='dimgray', width=3)
draw.ellipse((3 * w, 4 * w, 6 * w, 7 * w), 'white', outline='dimgray', width=3)
draw.ellipse((6 * w, 4 * w, 9 * w, 7 * w), 'white', outline='dimgray', width=3)
draw.ellipse((5.5 * w, 6 * w, 6.5 * w, 7 * w), nose, outline='dimgray', width=3)
draw.line((6 * w, 7 * w, 6 * w, 9 * w), 'dimgray', width=3)
draw.line((3 * w, 8 * w, 6 * w, 9 * w, 9 * w, 8 * w), 'dimgray', width=3)
draw.line((0, 7.5 * w, 4 * w, 7 * w, 0.5 * w, 8 * w), 'dimgray', width=3)
draw.line((w, 8.5 * w, 4 * w, 7 * w), 'dimgray', width=3)
draw.line((12 * w, 7.5 * w, 8 * w, 7 * w, 11.5 * w, 8 * w), 'dimgray', width=3)
draw.line((8 * w, 7 * w, 11 * w, 8.5 * w), 'dimgray', width=3)
draw.ellipse((4 * w, 5 * w, 5 * w, 6 * w), 'black')
draw.ellipse((7 * w, 5 * w, 8 * w, 6 * w), 'black')
im.save('cat.png')