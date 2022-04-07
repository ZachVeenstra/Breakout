import pygame as pg
from Ball import Ball

from Brick import Brick
from Overlay import Overlay
from Paddle import Paddle

class Game():
    """Sets up the environment, all of the balls, bricks paddle, etc.,
    and contains the game loop."""

    def __init__ (self):
        """Constructor"""
        pg.init()
        self.__screen = pg.display.set_mode((800,600))
        self.__clock = pg.time.Clock()
        self.__running = True
        self.__boxie = Brick()
        self.__overlay = Overlay()
        self.__paddle = Paddle()
        self.__overlay = Overlay()
        self.__paddle = Paddle()
        self.__balls = []



    def run(self):   
        while self.__running:

            # Event handling.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__running = False

            # Object Updating.
            self.__boxie.update()

            # Redrawing.
            self.__screen.fill((255,255,255))
            self.__boxie.draw(self.__screen)
            self.__overlay.draw(self.__screen)
            self.__paddle.draw(self.__screen)
            self.addBall()
            for ball in self.__balls:
                ball.draw(self.__screen)

            pg.display.flip()
            self.__clock.tick(60)

        # Quit the game when no longer running.    
        pg.quit()

    def addBall(self):
        """Adds a ball to the screen."""
        ball = Ball()
        self.__balls.append(ball)