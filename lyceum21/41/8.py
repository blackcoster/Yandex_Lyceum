import json

from PIL import Image

with open('task.json') as in_file:
    data = json.load(in_file)
im = Image.open('bottom.png')
crab = im.crop(data['crab'])
bubble = im.crop(data['bubble'])
im.paste(crab, data['paste'][:2])
im.paste(bubble, data['paste'][2:])
im.save('result.png')