from PIL import Image

im = Image.open('stone.png')
x, y = im.size

im_eyes = im.crop((115, 24, 188, 73))
im_eye = im.crop((115, 24, 152, 73))
gray = im.crop((39, 24, 114, 73))

im_temp = im.copy()
im_temp.paste(gray, (115, 24))

im_new = Image.new('RGB', (x * 5, y))
im_new.paste(im, (0, 0))

im1 = im_temp.copy()
im1.paste(im_eyes, (x // 2 - 37, 24))
im_new.paste(im1, (x, 0))

im2 = im_temp.copy()
im2.paste(im_eyes, (x - 188, 24))
im_new.paste(im2, (x * 2, 0))

im3 = im_temp.copy()
im3.paste(im_eye, (x - 188, 24))
im_new.paste(im3, (x * 3, 0))

im4 = im_temp.copy()
im4.paste(im_eye, (152, 24))
im_new.paste(im4, (x * 4, 0))

im_new.save('stones.png')
