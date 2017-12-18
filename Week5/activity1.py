"""
Week 5 - Activity 1: Order matters for animation
---------
AUTHOR: Edward Camp
"""
from cs1lib import *

WIDTH = 800
HEIGHT = 550

imageFiles = ['res/bush.png', 'res/darkClouds.png', 'res/flowers.png', 'res/grass.png', 'res/lightClouds.png',
              'res/mountains.png', 'res/road.png', 'res/sun.png', 'res/sky.png']
images = {}
imageQueue = []

def load_images():
    for filename in imageFiles:
        images[filename[4:-4]] = load_image(filename)

def draw_bush():
    imageQueue.append("bush")

def draw_darkClouds():
    imageQueue.append("darkClouds")

def draw_flowers():
    imageQueue.append("flowers")

def draw_grass():
    imageQueue.append("grass")

def draw_lightClouds():
    imageQueue.append("lightClouds")

def draw_mountains():
    imageQueue.append("mountains")

def draw_road():
    imageQueue.append("road")

def draw_sun():
    imageQueue.append("sun")

def draw_sky():
    imageQueue.append("sky")

def main_draw():
    clear()
    for imageKey in imageQueue:
        draw_image(images[imageKey], 0, 0)

"""
Activity Description:
Before diving into animation, it's important to understand that the order which we draw onto a canvas matters.
For example, in order to draw a door at the front of a house, we would first draw the house, and then the door. 
Drawing the door then the house would result in the house covering up the door; therefore the door wouldn't appear on
the canvas. For the activity below, there are nine images that must be drawn in the correct order to reveal a simple 
scene. Each image can be drawn by calling its corresponding 'draw' function. Please call and rearrange the nine 'draw'
functions to paint the scene.
"""

# ==============================
# ===== CODE ACTIVITY HERE =====
# ==============================

# Functions to call:


draw_sun()
draw_grass()
draw_bush()
draw_flowers()
draw_road()
draw_mountains()
draw_lightClouds()
draw_darkClouds()
draw_sky()


# ============================
# === END OF CODE ACTIVITY ===
# ============================

load_images()
start_graphics(main_draw, width=WIDTH, height=HEIGHT)
