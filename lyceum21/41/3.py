from PIL import Image

r, g, b = [int(x) for x in input().split()]
im = Image.open('input.png')
x, y = im.size
pixels = im.load()

im_new = Image.new('RGB', (x, 3 * y))
pix_new = im_new.load()

for i in range(x):
    for j in range(y):
        color = pixels[i, j]
        if color == (255, 255, 255):
            pix_new[i, j] = (r, g, b)
        else:
            pix_new[i, j] = pixels[i, j]

for i in range(x):
    for j in range(y):
        color = pixels[i, j]
        if color == (255, 255, 255):
            pix_new[i, j + y] = (g, r, b)
        else:
            pix_new[i, j + y] = pixels[i, j]

for i in range(x):
    for j in range(y):
        color = pixels[i, j]
        if color == (255, 255, 255):
            pix_new[i, j + 2*y] = (255, r-50, b-50)
        else:
            pix_new[i, j + 2*y] = pixels[i, j]

im_new.save('tomato.png')
