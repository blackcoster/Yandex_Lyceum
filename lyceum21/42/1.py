from turtle import Screen, done

from PIL import Image

sc = Screen()
im = Image.open('fon.png')
x, y = im.size
x0, y0 = (x - 768) // 2, (y - 648) // 2
im_new = im.crop((x0, y0, x0 + 768, y0 + 648))
im_new.save('f.png')
sc.setup(startx=0, starty=0)
sc.bgpic('f.png')
done()


