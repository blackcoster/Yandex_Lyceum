from PIL import Image

k = int(input())
with Image.open("flower.png") as im:
    im_ = im.resize((k, k))
    im_.save("icon.png")
