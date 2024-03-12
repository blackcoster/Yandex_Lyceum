from PIL import Image

w = int(input())
im = Image.open('tree.png')
im_new = im.crop((50, 50, 450, 450))
pix = im_new.load()
for i in range(400):
    for j in range(400):
        if pix[i, j] != (255, 255, 255):
            pix[i, j] = (w, w, w)

im_new = im_new.rotate(-90)
im_new = im_new.resize((400, 200))
im.paste(im_new, (300, 400))
im.save('shadow.png')