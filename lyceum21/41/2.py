from PIL import Image

im = Image.open('picture.png')
x, y = im.size
pixels = im.load()
n = int(input())
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        newr, newg, newb = max(0, r - n), max(0, g - n), max(0, b - n)
        pixels[i, j] = (newr, newg, newb)
im.save('result.png')
im.close()