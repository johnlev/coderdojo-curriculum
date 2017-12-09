"""
Week 1 activity: driving car
---------
AUTHOR: John Kotz
"""

# Import from the graphics library
from cs1lib import *
from math import *

# Constants
ROAD_WIDTH = 50
CAR_WIDTH = 15
CAR_HEIGHT = 25
WIDTH = 600
HEIGHT = 600
BLOCK_HEIGHT = HEIGHT / 4
LINE_HEIGHT = 10
LINE_WIDTH = 3
ANIMATION_LENGTH = 60
PARKING_LOT_HEIGHT = 40
HEADING_MAP = {'n': {'l': 'w', 'r': 'e'}, 'e': {'l': 'n', 'r': 's'}, 's': {'l': 'e', 'r': 'w'}, 'w': {'l': 's', 'r': 'n'}}

# Variables
action_queue = []
car_on = False
car_pos = (WIDTH / 2 + ROAD_WIDTH / 8 + CAR_WIDTH / 2, HEIGHT + CAR_HEIGHT / 2)
last_car_pos = car_pos
last_turn = None
car_heading = 'n'
car_angle = 0
last_car_angle = car_angle

current_action = 0
frame = -30

def draw():
    """

    :return:
    """
    set_framerate(ANIMATION_LENGTH / 2)
    set_clear_color(0, 1, 0)
    clear()

    set_fill_color(0.2, 0.2, 0.2)
    draw_rectangle(0, HEIGHT + PARKING_LOT_HEIGHT, WIDTH, -PARKING_LOT_HEIGHT)

    draw_road(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT)
    draw_intersection(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT)

    draw_road(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT, rotated=True)
    draw_road(WIDTH / 2 + ROAD_WIDTH / 2 + BLOCK_HEIGHT, HEIGHT - BLOCK_HEIGHT, rotated=True)
    draw_intersection(WIDTH / 2 + ROAD_WIDTH / 2 + BLOCK_HEIGHT, HEIGHT - BLOCK_HEIGHT)
    draw_intersection(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2, HEIGHT - BLOCK_HEIGHT)
    draw_road(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2, HEIGHT - BLOCK_HEIGHT - ROAD_WIDTH)
    draw_intersection(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH)
    set_fill_color(0, 0, 1)
    draw_circle(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2 + ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH - ROAD_WIDTH / 2, ROAD_WIDTH / 3)

    draw_road(WIDTH / 2 + BLOCK_HEIGHT + ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT - ROAD_WIDTH)
    draw_intersection(WIDTH / 2 + BLOCK_HEIGHT + ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH)
    draw_road(WIDTH / 2 + BLOCK_HEIGHT + ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH, rotated=True)
    draw_intersection(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH)
    draw_road(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH * 2)
    draw_intersection(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 3 - ROAD_WIDTH * 2)

    draw_road(WIDTH / 2 - ROAD_WIDTH / 2, HEIGHT - BLOCK_HEIGHT * 3 - ROAD_WIDTH * 2, rotated=True)
    draw_intersection(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2, HEIGHT - BLOCK_HEIGHT * 3 - ROAD_WIDTH * 2)
    draw_road(WIDTH / 2 - BLOCK_HEIGHT - ROAD_WIDTH * 3 / 2, HEIGHT - BLOCK_HEIGHT * 2 - ROAD_WIDTH * 2)

    global current_action
    if current_action < len(action_queue):

        global frame
        global car_pos
        global action
        global last_car_pos
        global last_car_angle
        global car_heading
        global car_angle
        global last_turn
        if frame < 10 or frame > ANIMATION_LENGTH - 10:
            # Do nothing
            pass
        else:
            # Move the car in the correct direction
            action = action_queue[current_action]

            if action == 'f':
                if car_heading == 'n' or car_heading == 's':
                    distance = abs(last_car_pos[1] - (BLOCK_HEIGHT + ROAD_WIDTH) * (-1 if car_heading == 's' else 1) - car_pos[1])

                    car_pos = (car_pos[0], car_pos[1] - distance / (ANIMATION_LENGTH - 9 - frame) * (-1 if car_heading == 's' else 1))
                if car_heading == 'e' or car_heading == 'w':
                    distance = abs(last_car_pos[0] + (BLOCK_HEIGHT + ROAD_WIDTH) * (-1 if car_heading == 'w' else 1) - car_pos[0])

                    car_pos = (car_pos[0] + distance / (ANIMATION_LENGTH - 9 - frame) * (-1 if car_heading == 'w' else 1), car_pos[1])
            else:
                distance = abs((last_car_angle - 90 * (-1 if action == 'r' else 1)) - car_angle)

                car_angle = car_angle - distance / (ANIMATION_LENGTH - 9 - frame) * (-1 if action == 'r' else 1)

        if frame >= ANIMATION_LENGTH:
            last_car_pos = car_pos
            last_car_angle = car_angle
            if action_queue[current_action] != 'f':
                car_heading = HEADING_MAP[car_heading][action_queue[current_action]]
                last_turn = action_queue[current_action]
            frame = 0
            current_action += 1
        else:
            frame += 1

    draw_car(car_pos, car_angle)


def draw_road(x, y, rotated=False):
    set_fill_color(0.2, 0.2, 0.2)
    set_stroke_color(0, 0, 0, 0)

    if not rotated:
        draw_rectangle(x, y, ROAD_WIDTH, -BLOCK_HEIGHT)
        for line in range(0, int(BLOCK_HEIGHT / LINE_HEIGHT / 2) + 1):
            set_fill_color(1, 1, 0)
            draw_rectangle(x + ROAD_WIDTH / 2 - LINE_WIDTH / 2, y - line * LINE_HEIGHT * 2, LINE_WIDTH, -LINE_HEIGHT)
    else:
        draw_rectangle(x, y, -BLOCK_HEIGHT, -ROAD_WIDTH)
        for line in range(0, int(BLOCK_HEIGHT / LINE_HEIGHT / 2) + 1):
            set_fill_color(1, 1, 0)
            draw_rectangle(x - line * LINE_HEIGHT * 2, y - ROAD_WIDTH / 2 + LINE_WIDTH / 2, -LINE_HEIGHT, -LINE_WIDTH)


def draw_intersection(x, y):
    set_fill_color(0.2, 0.2, 0.2)
    set_stroke_color(0, 0, 0, 0)

    draw_rectangle(x, y, ROAD_WIDTH, -ROAD_WIDTH)


def draw_car(pos, angle):
    x, y = pos

    points = []
    for i, j in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            tempX = j * CAR_WIDTH / 2
            tempY = i * CAR_HEIGHT / 2

            rotatedX = tempX * cos(radians(angle)) - tempY * sin(radians(angle))
            rotatedY = tempX * sin(radians(angle)) + tempY * cos(radians(angle))

            x1 = rotatedX + x
            y1 = rotatedY + y
            points.append((x1, y1))

    set_fill_color(1, 0, 1)
    draw_polygon(points)


def start():
    global car_on
    car_on = True


def move_forward():
    if car_on:
        action_queue.append('f')


def turn_left():
    if car_on:
        action_queue.append('l')


def turn_right():
    if car_on:
        action_queue.append('r')


def park():
    global car_on
    car_on = False


def done():
    start_graphics(draw, width=WIDTH, height=HEIGHT + PARKING_LOT_HEIGHT)


if __name__ == "__main__":
    done()
