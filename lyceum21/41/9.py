from PIL import Image

w = float(input())
im = Image.open('bird.png')
im1 = Image.open('dino.png')
x, y = im.size
pix = im.load()
pix1 = im1.load()
for i in range(x):
    for j in range(y):
        r, g, b = pix[i, j]
        r1, g1, b1 = pix1[i, j]
        pix[i, j] = int(min(w * r + (1 - w) * r1, 255)), \
            int(min(w * g + (1 - w) * g1, 255)), \
            int(min(w * b + (1 - w) * b1, 255))
im.save('origin.png')