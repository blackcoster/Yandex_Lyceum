from PIL import Image

n = int(input())
im = Image.open('clock.png')
w, h = im.size
im_new = Image.new('RGB', (w * n, h), 'white')
for i in range(n):
    temp = Image.new('RGB', (2 * w, 2 * h), 'white')
    temp.paste(im, (w // 2, h // 2))
    temp = temp.rotate(-30 * i)
    im_new.paste(temp.crop((w // 2, h // 2, 3 * w // 2, 3 * h // 2)), (i * w, 0))
im_new.save('ticking.png')
