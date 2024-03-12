from PIL import Image, ImageFilter

w = int(input())
im = Image.open('picture.png')
x, y = im.size
im_new = Image.new('RGB', (x, y * 2))
im_new.paste(im, (0, 0))
im1 = im.transpose(1)
im1 = im1.filter(ImageFilter.GaussianBlur(w))
im_new.paste(im1, (0, y))
im_new.save('result.png')