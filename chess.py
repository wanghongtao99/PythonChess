#!/usr/bin/python
# vim:fdm=marker
# Import..... {{{
from PIL import Image, ImageDraw, ImageFont
import ImageTk
import Tkinter
#}}}

Ch2Num = { "A" : 1,#{{{
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
      "P"  :  16,
      "Q"  :  17,
      "R"  :  18,
      "S"  :  19,
}
#}}}
Num2Ch = { 1   : "A", #{{{
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
    16  :  "P",
    17  :  "Q",
    18  :  "R",
    19  :  "S",
}
#}}}

class board_param:#{{{
  line_num    = 0
  size_grid   = 0

  size_board    = 0
                
  margin_left   = 0
  margin_down   = 0
  margin_right  = 0
  margin_up     = 0
                
                
  width_canvas  = 0
  height_canvas = 0
                
  board_tl_x    = 0
  board_tl_y    = 0
                
  board_dr_x    = 0
  board_dr_y    = 0
#}}}

def DrawChessBoard( line_num, size_grid):#{{{1

  # Init Board Parameters{{{
  boardParam = board_param()
  boardParam.line_num    = line_num;
  boardParam.size_grid   = size_grid;

  size_board    = size_grid * (line_num-1)

  margin_left   = size_grid
  margin_down   = size_grid
  margin_right  = size_grid/2
  margin_up     = size_grid/2


  width_canvas  = size_board + margin_left + margin_right
  height_canvas = size_board + margin_up + margin_down

  board_tl_x = margin_left
  board_tl_y = height_canvas - size_board - margin_down

  board_dr_x = margin_left + size_board
  board_dr_y = height_canvas - margin_down

  boardParam.size_board    = size_board

  boardParam.margin_left   = margin_left
  boardParam.margin_down   = margin_down
  boardParam.margin_right  = margin_right
  boardParam.margin_up     = margin_up


  boardParam.width_canvas  = width_canvas
  boardParam.height_canvas = height_canvas

  boardParam.board_tl_x    = board_tl_x
  boardParam.board_tl_y    = board_tl_y

  boardParam.board_dr_x    = board_dr_x
  boardParam.board_dr_y    = board_dr_y
  #}}}
  # draw Chess Bord {{{
  im = Image.new('RGBA', (width_canvas, height_canvas), "orange") # Create a blank image
  draw = ImageDraw.Draw(im) # Create a draw object
  draw.rectangle((board_tl_x, board_tl_y, board_dr_x,board_dr_y), fill="orange", outline="black")
  for i in range(1,14):
    draw.line((board_tl_x, i*size_grid+board_tl_y, board_dr_x, i*size_grid+board_tl_y),fill="black")
    draw.line((i*size_grid+board_tl_x, board_tl_y, i*size_grid+board_tl_x, board_dr_y),fill="black")

  font = ImageFont.truetype("arial.ttf", size_grid*2/4)

  for i in range(1,16):
    draw.text((margin_left - size_grid/6 + size_grid*(i-1), height_canvas - margin_down + size_grid/10),Num2Ch[i], fill="black", font=font)
  for i in range(1,16):
    draw.text((margin_left - size_grid*5/6, height_canvas - margin_down - size_grid/4 - (i-1)*size_grid), str(i), fill="black", font=font)

  def bigblack(x,y,radius=3, outline="black", fill="black"):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill, outline)

  bigblack( margin_left + 7 *size_grid,   height_canvas - margin_down - 7 *size_grid,   size_grid/6)
  bigblack( margin_left + 3 *size_grid,   height_canvas - margin_down - 3 *size_grid,   size_grid/6)
  bigblack( margin_left + 11*size_grid,   height_canvas - margin_down - 3 *size_grid,   size_grid/6)
  bigblack( margin_left + 3 *size_grid,   height_canvas - margin_down - 11*size_grid,  size_grid/6)
  bigblack( margin_left + 11*size_grid,   height_canvas - margin_down - 11*size_grid,  size_grid/6)
  #}}}
  return (im,boardParam)

def ChessmanCh2Cord( boardParam, HorCh, VerCh):#{{{1
  Cord_Grid_H = Ch2Num[HorCh]
  Cord_Grid_V = int(VerCh)
  
  Cord_Pixel_H = boardParam.margin_left + (Cord_Grid_H-1)*boardParam.size_grid
  Cord_Pixel_V = boardParam.height_canvas - boardParam.margin_down - (Cord_Grid_V - 1)*boardParam.size_grid

  return ( Cord_Pixel_H, Cord_Pixel_V)
def putBlackChessMan( im, boardParam, HorCh, VerCh):#{{{1
  (Cord_Pixel_H, Cord_Pixel_V) = ChessmanCh2Cord(boardParam, HorCh, VerCh)

  draw = ImageDraw.Draw(im) # Create a draw object
  def drawBlackChessMan(x,y,radius=7, outline="black", fill="black"):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill, outline)
  drawBlackChessMan(Cord_Pixel_H, Cord_Pixel_V, boardParam.size_grid*2/5)
def putWhiteChessMan( im, boardParam, HorCh, VerCh):#{{{1
  (Cord_Pixel_H, Cord_Pixel_V) = ChessmanCh2Cord(boardParam, HorCh, VerCh)

  draw = ImageDraw.Draw(im) # Create a draw object
  def drawWhiteChessMan(x,y,radius=7, outline="white", fill="white"):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill, outline)
  drawWhiteChessMan(Cord_Pixel_H, Cord_Pixel_V, boardParam.size_grid*2/5)

#Global {{{1

[im,boardParam] = DrawChessBoard( 15, 30)
putBlackChessMan(im, boardParam, "H","7")
putWhiteChessMan(im, boardParam, "H","8")
for i in ("A","B","C","D","E","F","G"):
  putWhiteChessMan(im,boardParam, i, 8)

root = Tkinter.Tk()  # A root window for displaying objects

# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(im)
Tkinter.Label(root, image=tkimage).pack() # Put it in the display window
Tkinter.Button(root).pack() # Put it in the display window
Tkinter.Button(root).pack() # Put it in the display window
root.mainloop() # Start the GUI

im.save("xxx.jpg")
