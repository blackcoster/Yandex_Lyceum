from turtle import Screen, done
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
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": geo,
              "format": "json"}

    url = "https://geocode-maps.yandex.ru/1.x?"

    response = requests.get(url, params=params).json()
    coordinates = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lonlat = ','.join(coordinates.split())

    params = {"apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
              "ll": lonlat,
              "z": int(z)}
    url = "https://static-maps.yandex.ru/v1?"
    response = requests.get(url, params=params)
    im = Image.open(BytesIO(response.content))
    #  сохраняем новую карту в новый файл
    im.save(f"map{z}.png")
    sc.bgpic(f"map{z}.png")

    sc.onkey(inc_scale, "Right")
    sc.onkey(dec_scale, "Left")

sc = Screen()
sc.setup(width=640, height=480)

geo = sc.textinput("Toponym", "Введите название местности")
z = sc.numinput("Scale", "Введите масштабный фактор от 1 до 21",
                    default=10, minval=1, maxval=21)
sc.listen()
draw_map()
done()