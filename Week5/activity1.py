"""
Week 5 - Activity 1: Bouncing Ball
---------
AUTHOR: Edward Camp
"""
from cs1lib import *

WIDTH = 800
HEIGHT = WIDTH * 9 / 16

"""
Activity Description:
Now that we know that the order which we draw objects on a canvas matters, we will now focus on movement of such
drawings on scene, otherwise known as animation. Animation can be defined as a sequence of still images that when
displayed quickly in a series. Changing the position/shape of an object in one image to the next can help convey
the motion of an object. In this activity, we will be changing the position of a ball to make it look as though it were
bouncing. The reality is that will be calculating the position of the ball depending on its speed at any point. Within
the Ball.py file, add the necessary code and functionality to the ball to allow it to bounce. Within the 'main_draw'
method, use the speed of the ball to change its position, and make it bounce against the top and bottom of the screen.
"""

"""
Second activity:
Give horizontal velocity 'vy' a numerical value other than 0 and implement bouncing behavior against the left and right
sides of the window.
"""

# Position of ball
x = WIDTH / 2
y = HEIGHT / 2

# Speed of ball
vx = 0
vy = -5

# Other information about the ball
radius = 30
red = 0.5
green = 1.0
blue = 0.0

# ANSWER SHOULD BE PUT INTO THIS FUNCTION
def main_draw():
    pass
    global x, y, vx, vy

    # Don't forget to set clear color and call clear
    set_clear_color(0.9, 0.9, 0.9)
    clear()

    # Change the position of the ball using the speed of the ball
    x = x + vx
    y = y + vy

    # If the position reaches off the top or bottom of the screen, change the speed of the ball to simulate a bounce.
    if y - radius < 0 and vy < 0:
        vy = -1 * vy
    elif y + radius > HEIGHT and vy > 0:
        vy = -1 * vy

    if x - radius < 0 and vx < 0:
        vx = -1 * vx
    elif x + radius > WIDTH and vx > 0:
        vx = -1 * vx

    # Draw the ball
    set_fill_color(red, green, blue)
    draw_circle(x, y, radius)

start_graphics(main_draw, width=WIDTH, height=HEIGHT, framerate=60)
