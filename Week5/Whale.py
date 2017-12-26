# Idea and spirtes taken from: https://scratch.mit.edu/projects/89605279/

from cs1lib import *
from Week5.WhaleFragment import WhaleFragment

class Whale:
    def __init__(self, canvasWidth, canvasHeight):
        self.mouseX = canvasWidth / 2
        self.mouseY = canvasHeight / 2

        self.lerpSpeed = 0.15
        self.distanceThreshold = 10
        self.frontView = True

        self.initSprites()

    def initSprites(self):
        self.sprites = []
        for i in range(1, 43):
            sprite = load_image("res/orca{}.png".format(i))
            self.sprites.append(WhaleFragment(sprite, self.mouseX, self.mouseY, sprite.width(), sprite.height()))

    def followMouse(self, mx, my):
        self.mouseX = mx
        self.mouseY = my - 50

    def toggleFrontView(self, key):
        if(key == 'b'):
            self.frontView = not self.frontView

    def lerp(self, a, b, t):
        t = min(1, max(t, 0))
        return a * (1 - t) + b * t

    def calculatePosition(self):
        # ANSWER STARTS HERE
        for i in range(len(self.sprites)):
            if i is 0:
                self.sprites[i].x = self.lerp(self.sprites[i].x, self.mouseX, self.lerpSpeed)
                self.sprites[i].y = self.lerp(self.sprites[i].y, self.mouseY, self.lerpSpeed)
            else:
                self.sprites[i].x = self.lerp(self.sprites[i].x, self.sprites[i - 1].x, self.lerpSpeed + i / 100 + 0.3)
                self.sprites[i].y = self.lerp(self.sprites[i].y, self.sprites[i - 1].y, self.lerpSpeed + i / 100 + 0.3)
        # ANSWER ENDS HERE


    def draw(self):
        # ANSWER STARTS HERE
        self.calculatePosition()

        if(self.frontView):
            for i in range(len(self.sprites) - 1, -1, -1):
                sprite = self.sprites[i]
                draw_image(sprite.img, sprite.x - sprite.width/2, sprite.y - sprite.height/2)

        else:
            for i in range(len(self.sprites)):
                sprite = self.sprites[i]
                draw_image(sprite.img, sprite.x - sprite.width / 2, sprite.y - sprite.height / 2)
        # ANSWER ENDS HERE
