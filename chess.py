#!/usr/bin/python
from PIL import Image, ImageDraw, ImageFont


line_num    = 15
size_grid = 20

size_board  =  size_grid * (line_num-1)

margin_left =size_grid
margin_down =size_grid
margin_right =size_grid/2
margin_up =size_grid/2


width_canvas  = size_board + margin_left + margin_right
height_canvas = size_board + margin_up + margin_down

board_tl_x = margin_left
board_tl_y = height_canvas - size_board - margin_down

board_dr_x = margin_left + size_board
board_dr_y = height_canvas - margin_down

im = Image.new('RGBA', (width_canvas, height_canvas), "white") # Create a blank image
draw = ImageDraw.Draw(im) # Create a draw object
draw.rectangle((board_tl_x, board_tl_y, board_dr_x,board_dr_y), fill="yellow", outline="red")
for i in range(1,14):
  draw.line((board_tl_x, i*size_grid+board_tl_y, board_dr_x, i*size_grid+board_tl_y),fill="black")
  draw.line((i*size_grid+board_tl_x, board_tl_y, i*size_grid+board_tl_x, board_dr_y),fill="black")

Ch2Num = { "A" : 1,
      "B"  :  2 ,
      "C"  :  3 ,
      "D"  :  4 ,
      "E"  :  5 ,
      "F"  :  6 ,
      "G"  :  7 ,
      "H"  :  8 ,
      "I"  :  9 ,
      "J"  :  10,
      "K"  :  11,
      "L"  :  12,
      "M"  :  13,
      "N"  :  14,
      "O"  :  15,
}
Num2Ch = { 1   : "A",
    2   :  "B",
    3   :  "C",
    4   :  "D",
    5   :  "E",
    6   :  "F",
    7   :  "G",
    8   :  "H",
    9   :  "I",
    10  :  "J",
    11  :  "K",
    12  :  "L",
    13  :  "M",
    14  :  "N",
    15  :  "O",

}
font = ImageFont.truetype("arial.ttf", size_grid*2/4)

for i in range(1,16):
  draw.text((margin_left - size_grid/6 + size_grid*(i-1), height_canvas - margin_down + size_grid/10),Num2Ch[i], fill="black", font=font)
for i in range(1,16):
  draw.text((margin_left - size_grid*5/6, height_canvas - margin_down - size_grid/4 - (i-1)*size_grid), str(i), fill="black", font=font)

def circle(x,y,radius=3, outline=0, fill="black"):
  draw.ellipse((x-radius, y-radius, x+radius, y+radius), outline, fill)

circle( margin_left + 7*size_grid,   height_canvas - margin_down - 7*size_grid,   size_grid/6)
circle( margin_left + 3*size_grid,   height_canvas - margin_down - 3*size_grid,   size_grid/6)
circle( margin_left + 11*size_grid,  height_canvas - margin_down - 3*size_grid,   size_grid/6)
circle( margin_left + 3*size_grid,   height_canvas - margin_down - 11*size_grid,  size_grid/6)
circle( margin_left + 11*size_grid,  height_canvas - margin_down - 11*size_grid,  size_grid/6)

im.save("xxx.jpg")
