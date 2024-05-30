from io import BytesIO
import requests
from PIL import Image

toponym = input()
params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym,
    "format": "json"
}
url = "https://geocode-maps.yandex.ru/1.x/?"
response = requests.get(url, params=params).json()
coordinates = response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]["Point"]["pos"]
lonlat = ','.join(coordinates.split())
static_url = f'https://static-maps.yandex.ru/v1?ll={lonlat}&z={6}&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
response = requests.get(static_url)
im = Image.open(BytesIO(response.content))
im.save(f"{toponym.lower()}.gif")