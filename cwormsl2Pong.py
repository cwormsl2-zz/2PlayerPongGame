from Ball import Ball
from Paddle import Paddle
from graphics import *
from time import sleep

"""
Caitlin Wormsley 12/14/12
This prgorams runs the game Pong while calling a Ball class and a Paddle class.
Along with the minimum requirements, this game has a background and is a two player version.
"""

class Pong:

    def __init__(self):
        #creates the window, the ball, the two paddles, and draws the background and the scoreboard.
        self.win = GraphWin("Pong", 800, 400)
        self.background = Image(Point(400,200),"pingpong.gif")
        self.background.draw(self.win)
        self.ball=Ball(self.win)
        self.paddle = Paddle(self.win,740,150,750,250,"red")
        self.paddle1 = Paddle(self.win, 60, 150,70,250,"blue")
        self.radius = self.ball.getRadius()

        self.scoreboard = Text(Point(400, 50), "")
        self.scoreboard.setSize(12)
        self.scoreboard.setTextColor("white")
        self.scoreboard.draw(self.win)
              
        y = 200
        self.middle = self.paddle.move(self.win, y)
        self.middle1 = self.paddle1.move(self.win,y)

                   
    def checkContact(self):
          #gets the values for the top and bottom of the paddles
          self.top = self.paddle.getMiddle()- (self.paddle.getHeight()/2)
          self.bot = self.paddle.getMiddle() +(self.paddle.getHeight()/2)

          self.top1 = self.paddle1.getMiddle() - (self.paddle1.getHeight()/2)
          self.bot1 = self.paddle1.getMiddle() + (self.paddle1.getHeight()/2)
          
          #gets the values of the left and right edges of the ball
          right = self.ball.getCenter().getX()+self.radius
          left = self.ball.getCenter().getX()-self.radius
          ballHeight = self.ball.getCenter().getY()

          touch = right - self.frontedge
          touch1 = self.frontedge1 - left
          
          #if the ball touches either paddle it returns true
          if (0 <= touch <= 10) or (0<= touch1 <= 10):
              if(self.top < ballHeight  <self.bot) and self.ball.moveRight():
                  return True
              elif (self.top1 < ballHeight < self.bot1) and self.ball.moveLeft():
                  return True
              else:
                  return False

    def gameOver(self):
        
        self.frontedge = self.paddle.getEdge()
        self.frontedge1 = self.paddle1.getEdge()
        ballWidth = self.ball.getCenter().getX()
        #returns true if the ball passes either of the paddles
        if (ballWidth > self.frontedge): 
            return True
        elif(ballWidth < self.frontedge1):
            return True
        else:
            return False

    
    def play(self):

        click = self.win.getMouse()
        y = click.getY()
        end = self.gameOver()
        contact = self.checkContact()
        self.hits = 0
        self.level = 1
       
       
        while not end:
          #moves the paddles based on the user's click point
          #if the ball is moving right the right paddle moves
          #if the ball is moving left the left paddle moves
          click = self.win.checkMouse()
          if click != None and  self.ball.moveRight():
            y = click.getY()
            self.paddle.move(self.win, y)
          elif click != None and self.ball.moveLeft():
            y = click.getY()
            self.paddle1.move(self.win, y)

          #moves the ball and reverses the X direction of the ball
          self.ball.move(self.win)
          sleep(0.025)
          contact = self.checkContact()
          if contact == True :
              self.ball.reverseX()
              self.hits = self.hits+1
              #increases ball speed after every 5 hits
              if self.hits%5==0:
                  self.ball.goFaster()
                  self.level=self.level+1

                  
          self.scoreboard.setText(("Hits:",self.hits, "Level:", self.level))   
          end = self.gameOver()

        self.scoreboard = Text(Point(400, 100),"You Lost")
        self.scoreboard.setSize(12)
        self.scoreboard.setTextColor("white")
        self.scoreboard.draw(self.win)
        self.win.getMouse()
        self.win.close()
        
                        
def main():

    p =Pong()
    p.play()
    
main()

        
