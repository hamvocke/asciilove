#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wand.image import Image
import argparse

parser = argparse.ArgumentParser(description='Turn an image into ascii art')
parser.add_argument('image', help='image path')
args = parser.parse_args()

symbols = {1.0: " ", 0.9: " ", 0.8: "░",  0.7: "░", 0.6: "▒", 0.5: "▒", 0.4:"▒", 0.3: "▓", 0.2: "▓", 0.1: "█", 0.0: "█"}

output = ""

def char_for_color(color):
    return symbols[round(color.red, 1)]

with Image(filename=args.image) as img:
    img.modulate(saturation=0)
    #img.level(black=0.2, white=0.8)
    #img.negate()
    img.resize(height=int(img.height//5), width=img.width//3)
    for row in img:
        for col in row:
            output += char_for_color(col)
        output += "\n"

print(output)