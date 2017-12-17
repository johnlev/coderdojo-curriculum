"""
Week 5 - Activity 2: Bouncing Ball
---------
AUTHOR: Edward Camp
"""

from cs1lib import *

"""
STEP 1: We will first code for movement of the ball. This behavior will added within the 'calculatePosition' method.
STEP 2: In order for the ball to bounce, it needs to bounce against something. In this case, we will code for this
        behavior within the 'checkBounce'. (Collision + Behavior after bounce)
STEP 3: Putting together the behaviors within the 'draw' method.

EXTRA 1: Include a method that will result in the ball to bounce when pressing a certain key.
EXTRA 2: Include a method that displays height of the ball next to it.
EXTRA 3: Add horizontal movement to the ball when a key is pressed
"""

class Ball():
    def __init__(self, x, y, radius, red, green, blue):
        self.x = x
        self.y = y
        self.radius = radius

        self.red = red
        self.green = green
        self.blue = blue

        self.vx = 0
        self.vy = 0

    def calculatePosition(self, gravity):
        # ANSWER
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy
        # END OF ANSWER

    def checkBounce(self, gravity, height):
        # ANSWER
        if self.y + self.radius > height and self.vy > 0:
            self.vy *= -0.9
            self.vy -= gravity * 1.05 # Correction to logic (Will fix later)
        # END OF ANSWER

    def draw(self, gravity, height):
        # ANSWER
        self.checkBounce(gravity, height)
        self.calculatePosition(gravity)

        set_fill_color(self.red, self.green, self.blue)
        draw_circle(self.x, self.y, self.radius)
        # END OF ANSWER
