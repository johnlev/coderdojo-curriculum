"""
Week 5 - Activity 3: Swimming Whale
---------
AUTHOR: Edward Camp
"""
from random import random

from Week5.AdvancedActivities.Bubble import Bubble

from Week5.AdvancedActivities.Whale import Whale
from cs1lib import *

"""
Activity Description:
Now that we know that the order which we draw objects on a canvas matters, we will now focus on movement of such
drawings on scene, otherwise known as animation. Animation can be defined as a sequence of still images that when
displayed quickly in a series. Changing the position/shape of an object in one image to the next can help convey
the motion of an object. In this activity, we will be animating stacked images of an orca as seen in the following
video (https://www.youtube.com/watch?v=i1fcVQhoz0U). If we are to move our mouse across the screen, the most front 
image of the orca will move towards the mouse, which the second image underneath the first will follow, which the third
image underneath will follow, and so on so forth. There are many ways to implement this movement which will be up to
you to code the behavior in the 'draw' and 'calculatePosition' method of Whale.py. Some suggestions maybe either
storing a list of previous movements to follow or using the 'lerp' function provided to delay the movement of other
fragments of the whale. In addition, you will code for the behavior of bubbles, which will be entirely up to you how
they should behave (e.g. rising up, waving around, randomly movement, etc.)
"""

WIDTH = 800
HEIGHT = WIDTH * 9 / 16

whale = Whale(WIDTH, HEIGHT)
bubbles = []

def addBubble():
    bubbles.append(Bubble(random() * WIDTH, random() * HEIGHT, WIDTH, HEIGHT))

def main_draw():
    set_clear_color(0, 0.6, 0.9)
    clear()

    whale.draw()
    for bubble in bubbles:
        bubble.draw()

for i in range(50):
    addBubble()
start_graphics(main_draw, width=WIDTH, height=HEIGHT, framerate=60, mouse_move=whale.followMouse, key_press=whale.toggleFrontView)
