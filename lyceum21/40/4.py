from PIL import Image
from PIL.ImageDraw import Draw

width = int(input())
w = int(input())
im = Image.new('RGB', (12 * w, 8 * w), 'white')
draw = Draw(im)
draw.arc((3 * w, 2 * w, 9 * w, 8 * w), -110, -70, fill='black', width=width)
draw.arc((3 * w, 2 * w, 9 * w, 8 * w), -1, 181, fill='black', width=width)
draw.arc((0, 0, 5 * w, 5 * w), 75, -5, fill='black', width=width)
draw.arc((7 * w, 0, 12 * w, 5 * w), -175, 105, fill='black', width=width)

draw.ellipse(((5 - 1 / 6) * w, (5 - 1 / 6) * w, (5 + 1 / 6) * w, (5 + 1 / 6) * w), 'black')
draw.ellipse(((7 - 1 / 6) * w, (5 - 1 / 6) * w, (7 + 1 / 6) * w, (5 + 1 / 6) * w), 'black')

draw.ellipse(((6 - 0.8) * w, (6 - 0.5) * w, (6 + 0.8) * w, (6 + 0.5) * w), 'black')

im.save('mouse.png')