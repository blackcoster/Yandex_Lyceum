from turtle import Screen, done
from io import BytesIO
from turtle import done, Screen
import requests
from PIL import Image


sc = Screen()
sc.setup(width=640, height=480)
geo = sc.textinput("Toponym", "Введите название местности")


params = {"apikey":"40d1649f-0493-4b70-98ba-98533de7710b",
          "geocode":geo,
          "format":"json"}

url = "https://geocode-maps.yandex.ru/1.x?"
response = requests.get(url,params=params).json()
coordinates = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
lonlat = ','.join(coordinates.split())

params = {"apikey":"f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
          "ll":lonlat,
          "z": 10}
url = "https://static-maps.yandex.ru/v1?"
response = requests.get(url,params=params)
im = Image.open(BytesIO(response.content))
#  сохраняем новую карту в новый файл
im.save(f"geo.png")
sc.bgpic(f"geo.png")
done()