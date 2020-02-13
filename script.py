#!/usr/bin/env python

from PIL import Image, ImageDraw
import os

image = os.path.expanduser("~") + "/Documents/PY_Image/ms.png"

im = Image.open(image)
width, height = im.size
draw = ImageDraw.Draw(im)


mx,my = width/2, height/2

r = width/10

ax = float(mx - r +0.001)
ay = int(my - r)
bx = int(mx + r)
by = int(my + r)

draw.ellipse([(ax,ay),(bx,by)],fill="red")

im.save(image,"PNG")

