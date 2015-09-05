from wand.image import Image, COLORSPACE_TYPES
from wand.display import display

symbols = {0.8: " ", 0.6: "░", 0.4:"▒", 0.2: "▓", 0.0: "█"}

output = ""

def char_for_color(color):
    for key in symbols:
        if color.red >= key:
            return symbols[key]
    return symbols[0.6]

with Image(filename='ham.jpg') as img:
    img.modulate(saturation=0)
    img.level(black=0.2, white=0.8)
    img.resize(height=img.height//3, width=img.width//3)
    for row in img:
        for col in row:
            output += char_for_color(col)
        output += "\n"

with open('output.txt', 'w') as f:
    f.write(output)
