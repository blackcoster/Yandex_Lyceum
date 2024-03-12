from PIL import Image

size = int(input())
color = input()
im = Image.open('portrait.png')
im1 = im.crop()
im_new = Image.new(im.mode, (im.width + 2 * size, im.height + 2 * size), color)
im_new.paste(im1, (size, size))
im_new.save('border.png')