from io import BytesIO
from turtle import done, Screen
import requests
from PIL import Image


def inc_scale():
    global z
    if z < 21:
        z += 1
    draw_map()


def dec_scale():
    global z
    if z > 1:
        z -= 1
    draw_map()


def draw_map():
    url = f'https://static-maps.yandex.ru/v1?ll={lonlat}&z={z}&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    response = requests.get(url)
    im = Image.open(BytesIO(response.content))
    #  сохраняем новую карту в новый файл
    im.save(f"football{z}.png")
    sc.bgpic(f"football{z}.png")
    sc.onkey(inc_scale, "Right")
    sc.onkey(dec_scale, "Left")


lonlat = "14.204317,68.149046"
z = 15
sc = Screen()
sc.setup(width=640, height=480)
sc.listen()
draw_map()
done()