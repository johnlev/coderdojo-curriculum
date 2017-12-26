from cs1lib import *
import random, math
from PyQt5.QtCore import *

# ADD NECESSARY FUCNTIONALITY / ANIMATION FOR ANIMATING BUBBLES
# class Bubble:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.loadSprite()
#
#     def loadSprite(self):
#         self.img = load_image('res/bubble.png')
#
#     def scale(self, scaleX, scaleY):
#         self.img.scaled(scaleX * self.img.width(), scaleY * self.img.height())
#
#     def draw(self):
#         pass
# END OF BASE


# A POTENTIAL ANSWER
class Bubble:
    def __init__(self, x, y, canvasWidth, canvasHeight):
        self.x = x
        self.y = y
        self.t = random.randint(0,360)

        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.xAmplitude = random.randint(10, 30)
        self.waveX = 0
        self.vy = random.random() * 3 + 1

        self.loadSprite()

    def loadSprite(self):
        self.img = load_image('res/bubble.png')
        self.original = load_image('res/bubble.png')

    def scale(self, scaleX, scaleY):
        self.img = self.original.scaled(scaleX * self.original.width(), scaleY * self.original.height(), Qt.IgnoreAspectRatio)

    def draw(self):
        # Vertical Movement
        self.y -= self.vy
        if(self.y < -100):
            self.y = self.canvasHeight + 100
            self.x = self.canvasWidth * random.random()

        # Trigonometry-based Calculations
        self.t += 1
        scaleX = 0.05 * math.sin(math.radians(self.t * 5.2 + 30)) + 0.3
        scaleY = 0.05 * math.cos(math.radians(self.t * 4.5 + 65)) + 0.3
        self.waveX = math.sin(math.radians(self.t * 3.9 + 22)) * self.xAmplitude

        self.scale(scaleX, scaleY)
        draw_image(self.img, self.x - self.img.width()/2 + self.waveX, self.y - self.img.height()/2)
# END OF POTENTIAL ANSWER