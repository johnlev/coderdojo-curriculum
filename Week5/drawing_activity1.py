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


def draw_dark_clouds():
    imageQueue.append("darkClouds")


def draw_flowers():
    imageQueue.append("flowers")


def draw_grass():
    imageQueue.append("grass")


def draw_light_clouds():
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
