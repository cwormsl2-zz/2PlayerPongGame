"""
Caitlin Wormsley 12/14/12
Paddle Constructor
"""
from graphics import *

class Paddle:

    def __init__(self, win, x1, y1, x2, y2,color):
       
        self.paddle = Rectangle (Point (x1, y1), Point(x2, y2))
        self.paddle.setFill(color)
        self.paddle.draw(win)
        self.frontedge = x1
        self.middle = 200
        self.height = 100
        
    


    def move(self, win, y):
        dy = y - self.middle
        self.paddle.move(0,dy)
        self.middle = y
        return self.middle

    def getMiddle(self):
        return self.middle

    def getHeight(self):
        return self.height

    def getEdge(self):
        return self.frontedge

    
    


def main():
  w = 300
  h = 300
  pWin = GraphWin("Pong", w, h )

  p = Paddle(pWin)

  while True:
    clickPoint = pWin.checkMouse()
    if clickPoint != None:
      y = clickPoint.getY()
      p.move(pWin, y)
 
  
  

  pWin.getMouse()
  pWin.close()
  

  
""" Only runs main if asked to run Paddle.py"""
if __name__ == '__main__':
    main()
