#!/usr/bin/env python

from wand.image import Image
import argparse

parser = argparse.ArgumentParser(description='Turn an image into ascii art')
parser.add_argument('image', help='image path')
args = parser.parse_args()

symbols = {0.8: " ", 0.6: "░", 0.4:"▒", 0.2: "▓", 0.0: "█"}

output = ""

def char_for_color(color):
    closest_key = next(iter(symbols.keys()))
    for key in symbols:
        if abs(color.red - key) < abs(color.red - closest_key):
            closest_key = key
    return symbols[closest_key]

with Image(filename=args.image) as img:
    img.modulate(saturation=0)
    #img.level(black=0.2, white=0.8)
    img.negate()
    img.resize(height=img.height//3, width=img.width//3)
    for row in img:
        for col in row:
            output += char_for_color(col)
        output += "\n"

print(output)
