import os
import sys

from PIL import Image, ImageDraw

file_name = sys.argv[1]
picture = Image.open(file_name)
WIDTH, HEIGHT = picture.size
draw = ImageDraw.Draw(picture)
text = f"{WIDTH} x {HEIGHT}"
text_width, text_height = draw.textsize(text)
text_bbox = draw.textbbox(
    (WIDTH - text_width - 10, HEIGHT - text_height - 20),
    text,
)
draw.text(text_bbox[:2], text, fill="white")
file_name_without_ext, ext = os.path.splitext(file_name)
new_file_name = f"{file_name_without_ext}-stamped{ext}"
picture.save(new_file_name)
