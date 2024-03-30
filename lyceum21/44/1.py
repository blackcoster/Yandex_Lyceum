from PIL import Image

n = int(input())
colors = []
for i in range(n):
    a = tuple([int(x) for x in input().split()])
    colors.append(a)

im = Image.open('leave0.png')
x, y = im.size
pix = im.load()

im_new = Image.new('RGB', (x * (n + 1), y))
im_new.paste(im, (0, 0))

for k in range(n):
    im_temp = Image.new("RGB", (x, y), 'white')
    pix_temp = im_temp.load()
    for i in range(x):
        for j in range(y):
            if pix[i, j] != (255, 255, 255):
                pix_temp[i, j] = colors[k]
    im_new.paste(im_temp, ((x * k + 100), 0))
im_new.save('leaves.png')

