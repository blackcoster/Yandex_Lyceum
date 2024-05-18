from io import BytesIO
from turtle import done, Screen
import requests
from PIL import Image



def mode_q():
    global spn
    spn = 1
    draw_map()

def mode_q():
    global spn
    spn = 1
    draw_map()

def mode_w():
    global spn
    spn = 0.5
    draw_map()

def mode_e():
    global spn
    spn = 0.25
    draw_map()

def mode_r():
    global spn
    spn = 0.125
    draw_map()

def mode_t():
    global spn
    spn = 0.0625
    draw_map()

def mode_y():
    global spn
    spn = 0.03125
    draw_map()

def draw_map():
    url = f'https://static-maps.yandex.ru/v1?ll={lonlat}&spn={spn},{spn}&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    response = requests.get(url)
    im = Image.open(BytesIO(response.content))
    #  сохраняем новую карту в новый файл
    im.save(f"football{spn}.png")
    sc.bgpic(f"football{spn}.png")
    sc.onkey(mode_q, "q")
    sc.onkey(mode_w, "w")
    sc.onkey(mode_e, "e")
    sc.onkey(mode_r, "r")
    sc.onkey(mode_t, "t")
    sc.onkey(mode_y, "y")


lonlat = "14.204317,68.149046"
spn = 1
sc = Screen()
sc.setup(width=640, height=480)
sc.listen()
draw_map()
done()