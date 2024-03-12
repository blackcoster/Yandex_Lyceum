from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
im = Image.new('RGB', (18 * w, 15 * w), 'white')
draw = Draw(im)
draw.ellipse((2 * w, w, 16 * w, 14 * w), outline='black', width=int(0.6 * w))
draw.arc((w, w, 6.5 * w, 7 * w), 120, -40, fill='black', width=int(0.8 * w))
draw.arc((11.5 * w, w, 17 * w, 7 * w), -140, 60, fill='black', width=int(0.8 * w))
draw.ellipse((3.5 * w, 7 * w, 6.5 * w, 11 * w), 'black')
draw.ellipse((11.5 * w, 7 * w, 14.5 * w, 11 * w), 'black')
draw.ellipse((4.5 * w, 8 * w, 5.5 * w, 9 * w), 'white')
draw.ellipse((12.5 * w, 8 * w, 13.5 * w, 9 * w), 'white')
draw.ellipse((8 * w, 9.5 * w, 10 * w, 10.5 * w), 'black')

im.save('panda.png')