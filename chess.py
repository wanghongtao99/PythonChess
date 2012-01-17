#!/usr/bin/python
# vim:fdm=marker
# Import..... {{{
from PIL import Image, ImageDraw, ImageFont
import ImageTk
import Tkinter
#}}}

# Global Variable  Ch2Num, Num2Ch {{{1
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
Num2Ch = {  1  : "A", #{{{
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
#}}}1

#  Classes #{{{1
## Class ChessBoard {{{2
class ChessBoard(Tkinter.Label):
  def __init__(self, parent):#{{{3


    self.boardParam = ComputParams(15,30)
    self.im = DrawChessBoard( self.boardParam )
    self.tkimage = ImageTk.PhotoImage(self.im)

    Tkinter.Label.__init__(self, parent, image=self.tkimage)
    self.parent = parent
    self.colorChess = "black"
    self.autoChangColor = 0
    self.NumOfStep = 1
    self.MarkStep = 0
    self.Steps = []
    self.BoardMap = {}
    self.initUI()

  def initUI(self):#{{{3

    self.parent.title("FIR")
    self.bind('<Button-1>',self.clickOnBoard)
    self.pack( expand=1)

    Button_black = Tkinter.Button(root, text="Black")
    Button_black.pack(side=Tkinter.LEFT)
    Button_black.bind('<Button-1>', self.clickBlackButton)

    Button_white = Tkinter.Button(root, text="White")
    Button_white.pack(side=Tkinter.LEFT)
    Button_white.bind('<Button-1>', self.clickBlackWhite)

    Button_auto  = Tkinter.Button(root, text="InTurn")
    Button_auto.pack(side=Tkinter.LEFT)
    Button_auto.bind('<Button-1>', self.clickBeginInTurn)

    Button_stop_auto  = Tkinter.Button(root, text="EndInTurn")
    Button_stop_auto.pack(side=Tkinter.LEFT)
    Button_stop_auto.bind('<Button-1>', self.clickEndInTurn)

    Button_save = Tkinter.Button(root, text="Save")
    Button_save.pack(side=Tkinter.LEFT)
    Button_save.bind('<Button-1>', self.clickBlackSave)

    Button_clear = Tkinter.Button(root, text="Clear")
    Button_clear.pack(side=Tkinter.LEFT)
    Button_clear.bind('<Button-1>', self.clickClear)

    Button_back = Tkinter.Button(root, text="back")
    Button_back.pack(side=Tkinter.LEFT)
    Button_back.bind('<Button-1>', self.clickBack)

  ###  Buttons {{{3
  def clickBlackSave(self, event):
    self.im.save("/tmp/abc.jpg")
  def clickBlackButton(self, event):
    self.colorChess = "black"

  def clickBlackWhite(self, event):
    self.colorChess = "white"

  def clickBeginInTurn(self, event):
    self.autoChangColor = 1
    self.MarkStep = 1

  def clickEndInTurn(self, event):
    self.autoChangColor = 0
    self.MarkStep = 0

  def clickClear(self, event):
    self.im = DrawChessBoard( self.boardParam)
    self.tkimage = ImageTk.PhotoImage(self.im)
    self.configure(image = self.tkimage)
    self.colorChess = "black"
    self.autoChangColor = 0
    self.NumOfStep = 1
    self.MarkStep = 0
    self.Steps = []


  def clickBack(self, event):
    StepRemove = self.Steps.pop()
    del self.BoardMap[StepRemove["Ch_H"] + StepRemove["Ch_V"]]
    self.reDrawBoardAndChesses()
    if self.NumOfStep > 0:
      self.NumOfStep -= 1
    if self.autoChangColor == 1:
      if self.colorChess == "white":
        self.colorChess = "black"
      else:
        self.colorChess = "white"

  def clickOnBoard(self, event):#{{{3

    if not PixelInBoard(self.boardParam, event.x, event.y):
      return

    (Ch_H, Ch_V) = Cord2ChessmanCh( self.boardParam, event.x, event.y)
    if self.BoardMap.get(Ch_H+Ch_V, 0) == 1:
      return
    self.BoardMap[Ch_H+Ch_V] = 1
    CurStep = {}
    CurStep["Ch_H"] = Ch_H
    CurStep["Ch_V"] = Ch_V
    CurStep["Color"] = self.colorChess
    CurStep["NumOfStep"] = -1
    if self.MarkStep == 1:
      CurStep["NumOfStep"] = self.NumOfStep
      putChessMan( self.im, self.boardParam, Ch_H, Ch_V, self.colorChess, str(self.NumOfStep))
      self.NumOfStep += 1
    else:
      putChessMan( self.im, self.boardParam, Ch_H, Ch_V, self.colorChess)

    self.Steps.append(CurStep)
    self.tkimage = ImageTk.PhotoImage(self.im)
    self.configure(image = self.tkimage)
    if self.autoChangColor == 1:
      if self.colorChess == "white":
        self.colorChess = "black"
      else:
        self.colorChess = "white"

  def reDrawBoardAndChesses(self):#{{{3
    self.im = DrawChessBoard( self.boardParam )
    for OneStep in self.Steps:
      if not OneStep["NumOfStep"] == -1:
        putChessMan( self.im, self.boardParam, OneStep["Ch_H"], OneStep["Ch_V"], OneStep["Color"], str(OneStep["NumOfStep"]))
      else:
        putChessMan( self.im, self.boardParam, OneStep["Ch_H"], OneStep["Ch_V"], OneStep["Color"])
    self.tkimage = ImageTk.PhotoImage(self.im)
    self.configure(image = self.tkimage)


#}}}2

## Class board_param {{{2
class board_param:
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

#}}}1

def ComputParams( line_num, size_grid):#{{{1

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

  boardParam = board_param()
  boardParam.line_num      = line_num;
  boardParam.size_grid     = size_grid;

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

  return boardParam
def DrawChessBoard( boardParam ):#{{{1

  # Init Board Parameters
  line_num    = boardParam.line_num;
  size_grid   = boardParam.size_grid;


  size_board    = boardParam.size_board

  margin_left   = boardParam.margin_left
  margin_down   = boardParam.margin_down
  margin_right  = boardParam.margin_right
  margin_up     = boardParam.margin_up


  width_canvas  = boardParam.width_canvas
  height_canvas = boardParam.height_canvas

  board_tl_x    = boardParam.board_tl_x
  board_tl_y    = boardParam.board_tl_y

  board_dr_x    = boardParam.board_dr_x
  board_dr_y    = boardParam.board_dr_y

  # draw Chess Bord
  im = Image.new('RGBA', (width_canvas, height_canvas), "orange") # Create a blank image
  draw = ImageDraw.Draw(im) # Create a draw object
  draw.rectangle((board_tl_x, board_tl_y, board_dr_x,board_dr_y), fill="orange", outline="black")
  for i in range(1,line_num - 1):
    draw.line((board_tl_x, i*size_grid+board_tl_y, board_dr_x, i*size_grid+board_tl_y),fill="black")
    draw.line((i*size_grid+board_tl_x, board_tl_y, i*size_grid+board_tl_x, board_dr_y),fill="black")

  font = ImageFont.truetype("arial.ttf", size_grid*2/4)

  for i in range(1,line_num + 1):
    draw.text((margin_left - size_grid/6 + size_grid*(i-1), height_canvas - margin_down + size_grid/10),Num2Ch[i], fill="black", font=font)
  for i in range(1,line_num + 1):
    draw.text((margin_left - size_grid*5/6, height_canvas - margin_down - size_grid/4 - (i-1)*size_grid), str(i), fill="black", font=font)

  def bigblack(x,y,radius=3, outline="black", fill="black"):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill, outline)

  x = margin_left + line_num/2 *size_grid
  y = height_canvas - margin_down - line_num/2 *size_grid
  bigblack( x, y, size_grid/6)
  x = margin_left + line_num/4 *size_grid
  y = height_canvas - margin_down - line_num/4 *size_grid
  bigblack( x, y, size_grid/6)
  x = margin_left + line_num*3/4 *size_grid
  y = height_canvas - margin_down - line_num/4 *size_grid
  bigblack( x, y, size_grid/6)
  x = margin_left + line_num/4 *size_grid
  y = height_canvas - margin_down - line_num*3/4 *size_grid
  bigblack( x, y, size_grid/6)
  x = margin_left + line_num*3/4 *size_grid
  y = height_canvas - margin_down - line_num*3/4 *size_grid
  bigblack( x, y, size_grid/6)

  return im
def ChessmanCh2Cord( boardParam, HorCh, VerCh):#{{{1
  Cord_Grid_H = Ch2Num[HorCh]
  Cord_Grid_V = int(VerCh)

  Cord_Pixel_H = boardParam.margin_left + (Cord_Grid_H-1)*boardParam.size_grid
  Cord_Pixel_V = boardParam.height_canvas - boardParam.margin_down - (Cord_Grid_V - 1)*boardParam.size_grid

  return ( Cord_Pixel_H, Cord_Pixel_V)

def Cord2ChessmanCh( boardParam, x, y):#{{{1
  Cord_Grid_H = ( (x + boardParam.size_grid/2 ) - boardParam.margin_left ) / boardParam.size_grid + 1
  Cord_Grid_V = ( boardParam.height_canvas - boardParam.margin_down - y + boardParam.size_grid/2 ) \
      / boardParam.size_grid + 1

  Ch_H = Num2Ch[Cord_Grid_H]
  Ch_V = str(Cord_Grid_V)
  return (Ch_H,Ch_V)

def PixelInBoard(boardParam, Cord_Pixel_H, Cord_Pixel_V): #{{{1
  margin_left = boardParam.margin_left
  size_board  = boardParam.size_board
  margin_up   = boardParam.margin_up
  if Cord_Pixel_H < margin_left - boardParam.size_grid/2 or \
      Cord_Pixel_H >= margin_left + size_board + boardParam.size_grid/2:
        return 0
  if Cord_Pixel_V < margin_up - boardParam.size_grid/2 or \
      Cord_Pixel_V >= margin_up + size_board + boardParam.size_grid/2:
        return 0
  return 1

def putChessMan( im, boardParam, HorCh, VerCh, Color, CharDisplay = None):#{{{1
  (Cord_Pixel_H, Cord_Pixel_V) = ChessmanCh2Cord(boardParam, HorCh, VerCh)

  if Color == "black":
    Ch_Color = "white"
  else:
    Ch_Color = "black"

  draw = ImageDraw.Draw(im) # Create a draw object
  def drawChessMan(x,y,radius, color):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), color, color)

  drawChessMan(Cord_Pixel_H, Cord_Pixel_V, boardParam.size_grid*2/5, Color)

  if not CharDisplay == None:
    fontsize = (boardParam.size_grid -4 )*3/4
    font = ImageFont.truetype("arial.ttf", fontsize)
    (char_width, char_height) = font.getsize(CharDisplay)
    #print (char_width, char_height)
    draw.text( (Cord_Pixel_H - char_width/2 , Cord_Pixel_V - char_height/2 + 1 ), CharDisplay, fill=Ch_Color, font=font)

#Global {{{1

root = Tkinter.Tk()  # A root window for displaying objects
chessBoard = ChessBoard(root)
root.mainloop() # Start the GUI
