from PIL import Image

colors = [tuple([int(x) for x in input().split()]) for line in range(int(input()))]
im = Image.open('star.png')
x, y = im.size
w, h = im.size
im_new = Image.new('RGB', (x * (len(colors) + 1), y), 'white')
im_new.paste(im, (0, 0))
for k in range(len(colors)):
    w = w * 2 // 3
    h = h * 2 // 3
    im.resize((w, h))
    pix = im.load()
    for i in range(w):
        for j in range(h):
            if pix[i, j] != (255, 255, 255):
                pix[i, j] = colors[k]

    temp = Image.new('RGB', (x, y), 'white')
    temp.paste(im, ((x - w) // 2, (y - h) // 2))
    im_new.paste(temp, (x * (k + 1), 0))
im_new.save('result.png')
