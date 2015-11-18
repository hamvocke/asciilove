# -*- coding: utf-8 -*-

import math
from wand.image import Image

symbols = {1.0: " ", 0.9: " ", 0.8: " ",  0.7: "░", 0.6: "░", 0.5: "▒", 0.4:"▒", 0.3: "▓", 0.2: "▓", 0.1: "█", 0.0: "█"}

def round(value):
    value = 0 if value < 0 else value
    return math.floor(math.fabs(value) * 10) / 10

def char_for_color(color):
    return symbols[round(color.red)]

def convert(image):
    output = ""
    with Image(filename=image) as img:
        img.modulate(saturation=0)
        #img.level(black=0.2, white=0.8)
        #img.negate()
        img.resize(height=int(img.height//5), width=img.width//3)
        for row in img:
            for col in row:
                output += char_for_color(col)
            output += "\n"

    return output