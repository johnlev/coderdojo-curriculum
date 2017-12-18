"""
Week 6 - Activity: Simple Pong
---------
AUTHOR: Edward Camp
"""

"""
Activity Description:
Last week, we covered that the order which elements are drawn on a canvas matters and that we can convey motion on
screen by changing the position/shape of an element drawn on a canvas (animation). This week, we'll be expanding on
animation by creating a simple game of pong. The main game loop has already been programmed and will function correctly
once we code the appropriate behaviors for the Paddle and Ball class. For this activity, follow the steps below to
create Pong.


STEPS TO CODING PONG:
STEP 1: Before anything else, we should get some elements to appear onscreen. For both Ball.py and Paddle.py, write
some code that will draw these objects on screen within their respective 'draw' method.

STEP 2: Next, we'll be animating the ball. Each time a ball is spawned, it is assigned a random x and y speed.
Utilizing these properties of the Ball, change the position of the ball accordingly within the 'calculatePosition'
method of Ball.py.

STEP 3: Now we'll be animating the movement of the paddles. This is done by setting the speed of the paddle when a
key is pressed and changing the position of the paddle accordingly. In addition, if a key is released, then the speed
should be set to 0. Code this behavior within the 'movePaddleUp', 'movePaddleDown', 'stopPaddle', and 
'calculatePosition' methods in Paddle.py. Make certain that the paddles don't travel off-screen.

STEP 4: At this point, we have animated the ball and paddles for pong. However, you probably have noticed that the ball
does not collide against anything in the scene. If a ball were to collide with either against any objects in the scene, 
we should expect that either the x or y speed of the ball to be inverted (kinda like how a ball bounces). For
this step, we will first add the behavior of the ball colliding against the horizontal wall of the screen in the
'wallBounce' method in Ball.py. Afterwards, we will add ball-paddle collision detection in the 'checkCollision' method 
in Paddle.py and then code the appropriate bouncing behavior in the 'paddleBounce' method in Ball.py.

STEP 5: We're almost done. Now that we've added interactivity between elements on screen, it's time to reward players
points. If a ball were to fly off-screen past either paddle, we should give a point to the appropriate player. Within
the 'checkGoal' method in Ball.py, reward the correct player when the ball goes off-screen using the
'game.reward_left_paddle(ball)' and 'game.reward_right_paddle(ball)' method calls.
"""

from cs1lib import *
from Week6.Ball import Ball
from Week6.Paddle import Paddle

class PongGame:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = self.WIDTH * (9/16)

        self.leftPoints = 0
        self.leftFontSize = 25

        self.rightPoints = 0
        self.rightFontSize = 25

        self.winningPoint = 7
        self.gameFinished = False
        self.winnerMessage = "{} Wins!"

    def reward_left_paddle(self, ball):
        ballList.remove(ball)
        ballList.append(Ball(game.WIDTH / 2, game.HEIGHT / 2, 10, 0.8, 0.2, 0, game))
        self.leftPoints += 1
        self.leftFontSize = 50

        if(self.leftPoints >= self.winningPoint):
            self.gameFinished = True
            self.winnerMessage = self.winnerMessage.format("Left Paddle")

    def reward_right_paddle(self, ball):
        ballList.remove(ball)
        ballList.append(Ball(game.WIDTH / 2, game.HEIGHT / 2, 10, 0.8, 0.2, 0, game))
        self.rightPoints += 1
        self.rightFontSize = 50

        if(self.rightPoints >= self.winningPoint):
            self.gameFinished = True
            self.winnerMessage = self.winnerMessage.format("Right Paddle")

    def key_pressed(self, key):
        if(key == 'a'):
            leftPaddle.movePaddleUp()
        if(key == 'z'):
            leftPaddle.movePaddleDown()
        if(key == 'k'):
            rightPaddle.movePaddleUp()
        if(key == 'm'):
            rightPaddle.movePaddleDown()

    def key_released(self, key):
        if(key == 'a'):
            leftPaddle.stopPaddle()
        if(key == 'z'):
            leftPaddle.stopPaddle()
        if(key == 'k'):
            rightPaddle.stopPaddle()
        if(key == 'm'):
            rightPaddle.stopPaddle()

    def lerp(self, a, b, t):
        return a * (1 - t) + b * t

    def draw(self):
        set_clear_color(0.05, 0.05, 0.05)
        clear()

        if(not self.gameFinished):
            set_font_bold()
            set_stroke_color(1,1,1)
            self.leftFontSize = self.lerp(self.leftFontSize, 25, 0.2)
            set_font_size(self.leftFontSize)
            draw_text(str(self.leftPoints),
                      100 - get_text_width(str(self.leftPoints)) / 2,
                      50 + get_text_height()/3)

            self.rightFontSize = self.lerp(self.rightFontSize, 25, 0.2)
            set_font_size(self.rightFontSize)
            draw_text(str(self.rightPoints),
                      (self.WIDTH - 100) - get_text_width(str(self.leftPoints)) / 2,
                      50 + get_text_height()/3)
            set_stroke_color(0,0,0)

            for ball in ballList:
                ball.wallBounce()
                ball.checkGoal()
                ball.calculatePosition()
                ball.draw()

                leftPaddle.checkCollision(ball)
                rightPaddle.checkCollision(ball)

            leftPaddle.calculatePosition()
            rightPaddle.calculatePosition()

            leftPaddle.draw()
            rightPaddle.draw()

        else:
            set_font_bold()
            set_stroke_color(1,1,1)
            set_font_size(50)
            draw_text(self.winnerMessage,
                      self.WIDTH / 2 - (get_text_width(self.winnerMessage) / 2),
                      self.HEIGHT / 2 + (get_text_height() / 3))


enable_smoothing()
game = PongGame()

ballList = []
ballList.append(Ball(game.WIDTH / 2, game.HEIGHT / 2, 10, 0.8, 0.2, 0, game))

leftPaddle = Paddle(10, game.HEIGHT / 2, 20, 100, 0.2, 0.9, 0.1, 'left', game)
rightPaddle = Paddle(game.WIDTH - 40, game.HEIGHT / 2, 20, 100, 0, 0.3, 0.9, 'right', game)


start_graphics(game.draw, width=game.WIDTH, height=game.HEIGHT, framerate=60,
               key_press=game.key_pressed, key_release=game.key_released)