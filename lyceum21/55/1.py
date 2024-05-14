from io import BytesIO

import requests
from PIL import Image


# url='https://geocode-maps.yandex.ru/1.x/?format=json&apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode= Санкт-петербург Льва Толстого,16'

import requests

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"  # ваш ключ
longlat = input()
params = {
    "apikey": API_KEY,
    "geocode": longlat,
    "format": "json"
}
url = "https://geocode-maps.yandex.ru/1.x/?"
response = requests.get(url, params=params).json()




address = response["response"]["GeoObjectCollection"]["featureMember"][0][
    "GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
print(address)

