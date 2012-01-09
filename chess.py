#!/usr/bin/python

from PIL import Image, ImageDraw
im = Image.new('RGBA', (100, 100), (0, 0, 0, 0)) # Create a blank image
draw = ImageDraw.Draw(im) # Create a draw object
draw.rectangle((10, 10, 90, 90), fill="yellow", outline="red")
