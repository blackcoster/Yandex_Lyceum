from PIL import Image
from PIL.ImageDraw import Draw

w = int(input())
im = Image.new('RGB', (22 * w, 18 * w), 'ivory')
draw = Draw(im)
draw.polygon((3 * w, 0, 7 * w, 2 * w,
              3 * w, 5 * w), 'white',
             outline='black', width=12)
draw.polygon((19 * w, 0, 15 * w, 2 * w,
              19 * w, 5 * w), 'white',
             outline='black', width=12)
draw.ellipse((w, w, 21 * w, 18 * w), 'white')
draw.arc((w, w, 21 * w, 18 * w), -118, -62, fill='black', width=12)
draw.arc((w, w, 21 * w, 18 * w), -40, 220, fill='black', width=12)
draw.ellipse((5.5 * w, 10.5 * w, 6.5 * w, 12 * w), 'black')
draw.ellipse((15.5 * w, 10.5 * w, 16.5 * w, 12 * w), 'black')
draw.ellipse((9.5 * w, 12 * w, 12.5 * w, 14 * w), 'black')
for a, b, c, d in [(0, 12, 3, 11.5), (1, 14, 3.5, 12.5),
                   (2.5, 15, 4, 13.5), (22, 12, 19, 11.5),
                   (21, 14, 18.5, 12.5), (19.5, 15, 18, 13.5)]:
    draw.line((a * w, b * w, c * w, d * w), fill='black', width=12)
im.save('kitty.png')