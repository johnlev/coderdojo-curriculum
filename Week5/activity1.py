from Week5.drawing_activity1 import *

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


draw_sky()
draw_dark_clouds()
draw_light_clouds()
draw_sun()
draw_mountains()
draw_grass()
draw_bush()
draw_flowers()


# ============================
# === END OF CODE ACTIVITY ===
# ============================

load_images()
start_graphics(main_draw, width=WIDTH, height=HEIGHT)
