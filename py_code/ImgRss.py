import PIL
from PIL import Image, ImageDraw, ImageFont
import os

turret = Image.open("./image/turret.png")
box = (0,0,30,30)

turret.crop(box).save("headTurret.png")
turret_crop = Image.open("./headTurret.png")