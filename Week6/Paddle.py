"""
Week 6 - Paddle Class
---------
AUTHOR: Edward Camp
"""

from cs1lib import *

class Paddle:
    def __init__(self, x, y, width, height, r, g, b, paddleName, game):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.r = r
        self.g = g
        self.b = b

        self.paddleName = paddleName

        self.vy = 0
        self.velocity = 10

    def checkCollision(self, ball):
        # The collision detection is geometrically incorrect, but simple enough for it to be functional
        # ANSWER STARTS HERE
        if(self.x < ball.x < self.x + self.width  and  self.y < ball.y < self.y + self.height):
            ball.paddleBounce(self.paddleName)
        # ANSWER ENDS HERE

    def movePaddleUp(self):
        self.vy = -self.velocity        # ANSWER IS ONE LINE

    def movePaddleDown(self):
        self.vy = self.velocity         # ANSWER IS ONE LINE

    def stopPaddle(self):
        self.vy = 0                     # ANSWER IS ONE LINE

    def calculatePosition(self):
        # ANSWER STARTS HERE
        if(self.y < 0):
            self.y = 0
        elif(self.y + self.height > self.game.HEIGHT):
            self.y = self.game.HEIGHT - self.height
        else:
            self.y += self.vy
        # ANSWER ENDS HERE


    def draw(self):
        # ANSWER STARTS HERE
        set_fill_color(self.r, self.g, self.b)
        draw_rectangle(self.x, self.y, self.width, self.height)
        # ANSWER ENDS HERE
