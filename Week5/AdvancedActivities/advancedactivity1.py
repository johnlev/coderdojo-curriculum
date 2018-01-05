"""
Week 5 - Activity 2: Bouncing Ball
---------
AUTHOR: Edward Camp
"""
import random

from Week5.AdvancedActivities.Ball import Ball
from cs1lib import *

WIDTH = 800
HEIGHT = 550
GRAVITY = 1

ballList = []


def add_ball(x=None, y=None, rad=None, r=None, g=None, b=None):
    x = random.uniform(0, WIDTH) if x is None else x
    y = random.uniform(50, 300) if y is None else y
    rad = random.uniform(10, 30) if rad is None else rad
    r = random.uniform(0, 1) if r is None else r
    g = random.uniform(0, 1) if g is None else g
    b = random.uniform(0, 1) if b is None else b

    ballList.append(Ball(x, y, rad, r, g, b))


def main_draw():
    clear()
    for ball in ballList:
        ball.draw(GRAVITY, HEIGHT)

"""
Activity Description:
Now that we know that the order which we draw objects on a canvas matters, we will now focus on movement of such
drawings on scene, otherwise known as animation. Animation can be defined as a sequence of still images that when
displayed quickly in a series. Changing the position/shape of an object in one image to the next can help convey
the motion of an object. In this activity, we will be changing the position of a ball to make it look as though it were
bouncing. The reality is that will be calculating the position of the ball depending on its speed at any point. Within
the Ball.py file, add the necessary code and functionality to the ball to allow it to bounce.
"""

for i in range(0, 10):
    add_ball()
start_graphics(main_draw, width=WIDTH, height=HEIGHT, framerate=60)
