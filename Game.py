import pygame as pg
from Ball import Ball

from Brick import Brick
from Overlay import Overlay
from Paddle import Paddle

class Game():
    """Sets up the environment, all of the balls, bricks paddle, etc.,
    and contains the game loop.
    """

    def __init__ (self):
        """Constructor"""
        pg.init()

        # The screen width in height, measured by pixels.
        self.__SCREEN_WIDTH = 800
        self.__SCREEN_HEIGHT = 600

        # The rows and columns of bricks.
        self.__ROWS = 5
        self.__COLUMNS = 8

        # The width and height of bricks. The bricks should take up the 
        # top half of the screen.
        self.__BRICK_WIDTH = self.__SCREEN_WIDTH / self.__COLUMNS
        self.__BRICK_HEIGHT = self.__SCREEN_HEIGHT / self.__ROWS / 2

        # Sets the width and height of the screen
        self.__screen = pg.display.set_mode((self.__SCREEN_WIDTH,
                                             self.__SCREEN_HEIGHT))

        self.__clock = pg.time.Clock()

        self.__running = True

        self.__bricks  = []

        self.__balls = []

        self.__overlay = Overlay()

        self.__paddle = Paddle()

        self.__overlay = Overlay()

        self.__paddle = Paddle()





    def run(self):   

        self.addBall()

        # Loops through the x and y variables each brick will occupy.
        for x in range(0, int(self.__COLUMNS * self.__BRICK_WIDTH), int(self.__BRICK_WIDTH)):
            for y in range(0, int(self.__ROWS * self.__BRICK_HEIGHT), int(self.__BRICK_HEIGHT)):
                self.addBrick(self.__BRICK_WIDTH, self.__BRICK_HEIGHT, x, y)

        while self.__running:

            # Event handling.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__running = False

            

            # Redrawing.
            self.__screen.fill((255,255,255))
            
            self.__paddle.draw(self.__screen)
            

            for brick in self.__bricks:
                brick.draw(self.__screen)

            for ball in self.__balls:
                ball.draw(self.__screen)

            self.__overlay.draw(self.__screen)

            pg.display.flip()
            self.__clock.tick(60)

        # Quit the game when no longer running.    
        pg.quit()

    def addBall(self):
        """Adds a ball to the list of balls so that multiple
        may appear on the screen.
        """

        ball = Ball()
        self.__balls.append(ball)

    def addBrick(self, width, height, x, y):
        """Adds a brick to the list of bricks so that multiple may
        appear on the screen.
        """

        brick = Brick(width, height, x, y)
        self.__bricks.append(brick)

    def getWidth(self):
        return self.__SCREEN_WIDTH
