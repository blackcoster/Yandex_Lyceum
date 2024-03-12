from PIL import Image, ImageFilter

w = int(input())
forest = Image.open('forest.png')
x, y = forest.size
hedgehog = Image.open('hedgehog.png')
a, b = hedgehog.size
hedgehog = hedgehog.resize((a // 2, b // 2))
forest.paste(hedgehog, (w, y - b // 2))
forest = forest.filter(ImageFilter.BLUR)

forest.save('hedgehog_in_fog.png')