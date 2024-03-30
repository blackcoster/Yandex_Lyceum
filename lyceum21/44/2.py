from PIL import Image

n = int(input())

im = Image.open('flower.png')
images = [im]
x, y = im.size
in_new = Image.new('RGB', (x * (n + 1), y))
temp = im.copy()

for _ in range(n):
    im_temp = Image.new('RGB', (x, y), 'white')
    w, h = temp.size
    a = w // n * (n - 1)
    b = h // n * (n - 1)
    temp = temp.resize((a, b))
    im_temp.paste(temp, ((x - a) // 2, (y - b) // 2))
    images.append(im_temp)

for i in range(n + 1):
    in_new.paste(images[n - i], (x * i, 0))

in_new.save('flowers.png')
