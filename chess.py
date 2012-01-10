#!/usr/bin/python
from PIL import Image, ImageDraw

width_canvas  =320
height_canvas =320

width_board  =280
height_board =280

margin_left =30
margin_down =30

board_tl_x = margin_left
board_tl_y = height_canvas - height_board - margin_down

board_dr_x = margin_left + width_board
board_dr_y = height_canvas - margin_down
im = Image.new('RGBA', (width_canvas, height_canvas), "white") # Create a blank image
draw = ImageDraw.Draw(im) # Create a draw object
draw.rectangle((board_tl_x, board_tl_y, board_dr_x,board_dr_y), fill="yellow", outline="red")
for i in range(1,14):
  draw.line((board_tl_x, i*20+board_tl_y, board_dr_x, i*20+board_tl_y),fill="black")
  draw.line((i*20+board_tl_x, board_tl_y, i*20+board_tl_x, board_dr_y),fill="black")
im.save("xxx.jpg")
