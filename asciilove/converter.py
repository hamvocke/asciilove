# -*- coding: utf-8 -*-

import math
from wand.image import Image

symbols = {1.0: u" ", 0.9: u" ", 0.8: u" ",  0.7: u"░", 0.6: u"░", 0.5: u"▒", 0.4: u"▒", 0.3: u"▓", 0.2: u"▓", 0.1: u"█", 0.0: u"█"}

def round(value):
    value = 0 if value < 0 else value
    return math.floor(math.fabs(value) * 10) / 10

def char_for_color(color):
    return symbols[round(color.red)]

def convert(image, negative=False):
    output = ""
    with Image(filename=image) as img:
        img.modulate(saturation=0)
        if(negative):
            img.negate()
        img.resize(height=int(img.height//5), width=img.width//3)
        for row in img:
            for col in row:
                output += char_for_color(col)
            output += "\n"

    return output
