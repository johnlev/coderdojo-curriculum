"""
Week 6 - Activity: Simple Pong
---------
AUTHOR: Edward Camp
"""

from cs1lib import *
import random

class Ball:
    def __init__(self, x, y, radius, r, g, b, game):
        self.game = game
        self.x = x
        self.y = y
        self.radius = radius

        self.r = r
        self.g = g
        self.b = b

        self.vx = (random.uniform(2.0, 4.5)) * (1 if random.randint(0,1) == 1 else -1)
        self.vy = random.uniform(-3.0, 3.0)
        self.acceleration = 1.025

    def paddleBounce(self, paddleName):
        pass
        # ANSWER STARTS HERE
        if(paddleName == 'left' and self.vx < 0):
            self.vx *= -1 * self.acceleration
        elif(paddleName == 'right' and self.vx > 0):
            self.vx *= -1 * self.acceleration
        # ANSWER ENDS HERE

    def wallBounce(self):
        pass
        # ANSWER STARTS HERE
        if(self.y < 0 and self.vy < 0):
            self.vy *= -1
        elif(self.y > self.game.HEIGHT and self.vy > 0):
            self.vy *= -1
        # ANSWER ENDS HERE

    def checkGoal(self):
        pass
        if(self.x < 0):                     # ANSWER IS CONDITIONAL
            self.game.reward_right_paddle(self)
        elif(self.x > self.game.WIDTH):     # ANSWER IS CONDITIONAL
            self.game.reward_left_paddle(self)

    def calculatePosition(self):
        pass
        # ANSWER STARTS HERE
        self.x += self.vx
        self.y += self.vy
        # ANSWER ENDS HERE

    def draw(self):
        pass
        # ANSWER STARTS HERE
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)
        # ANSWER ENDS HERE
