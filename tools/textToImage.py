#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import tools.fileProcessor as fp
import settings

def drawImage(imgFile):
    people = fp.readFile(settings.PEOPLE_LIST)
    dead = fp.readFile(settings.DEAD_LIST)

    img = Image.new('RGB', (1080, 720), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="/usr/share/fonts/truetype/freefont/FreeSerif.ttf", size=25)
    color = (0, 0, 0)
    x = 80
    y = 70

    for person in people:
        if y >= 670:
            x += 350
            y = 70
        if person in dead:
            color = (255, 0, 0)
        draw.text((x, y), person, fill=color, font=font)
        color = (0, 0, 0)
        y += 32
    img.save(imgFile, "png")
