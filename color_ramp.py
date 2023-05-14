# Mini Proyecto: Rampas de color
from PIL import Image, ImageDraw

color_ramps = Image.new("RGB", (256, 256), "white")
draw = ImageDraw.Draw(color_ramps)

for x in range(256):
    for y in range(256):
        r = x
        g = y
        b = (x + y) // 2
        draw.rectangle([(x, y), (x + 1, y + 1)], fill=(r, g, b))
color_ramps.show()
