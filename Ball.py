"""
Caitlin Wormsley 12/14/12
Ball Constructor 
"""
from time import sleep
from random import randrange, random
from graphics import *

"""
Class Definition for Ball class

"""
class Ball:

	def __init__(self, win):
	  center = Point(400, 200)
	  self.circ = Circle(center, 30)
	  self.circ.setFill("white")
	  self.circ.draw(win)
	  
	  self.dx = randrange(2,4)
	  self.dy = randrange(2,4)

	def getCenter(self):
	  return self.circ.getCenter()
		
	def getRadius(self):
	  return self.circ.getRadius()
	
	def goFaster(self):
	  self.dx = self.dx * (1+random())
	  self.dy = self.dy *(1+random())
	
	#ADD TO PROGRAM DESCRIPTION
	def reverseX(self):
	  self.dx = self.dx * -1
	
	def reverseY(self):
	  self.dy = self.dy * -1
	
	def move(self, win):
	
	  winHeight = win.getHeight()
	  winWidth = win.getWidth()
	
	  topEdge = self.getCenter().getY() - self.getRadius()
	  bottomEdge = self.getCenter().getY() + self.getRadius()
	  leftEdge = self.getCenter().getX() - self.getRadius()
	  rightEdge = self.getCenter().getX() + self.getRadius()

	  if topEdge + self.dy < 0:
	    self.reverseY()
	  if bottomEdge +self.dy > winHeight:
	    self.reverseY()
	  if leftEdge + self.dx < 0:
	    self.reverseX()
	  if rightEdge + self.dx > winWidth:
	    self.reverseX()
	  
	  self.circ.move(self.dx, self.dy)

	def moveRight(self):
          if self.dx > 0:
            return True
          else:
            return False
        def moveLeft(self):
          if self.dx < 0:
            return True
          else:
            return False

		
"""
Test Code for Using Ball class
Note: this code is not "inside" the Ball class definition
Note: to use this call in your Pong game, make sure that
  1) the Ball.py file is in the same directory as your Pong.py file
  2) you type "from Ball import Ball" at the top of your Pong.py file
"""

def main():
  w = 300
  h = 300
  pWin = GraphWin("Pong", w, h )

  b = Ball(pWin)
  b2=Ball(pWin)
  
  cnt = 0
  while pWin.checkMouse() == None:
    b.move(pWin)
    b2.move(pWin)
    cnt = cnt+1
    sleep(0.01)
    if cnt % 100 == 0:
      b.goFaster()
    
  pWin.getMouse()
  pWin.close()
  
  
  
  
""" Only runs main if asked to run Ball.py"""
if __name__ == '__main__':
    main()
