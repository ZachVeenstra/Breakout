import pygame as pg

from pygame import mixer
from Ball import Ball
from Brick import Brick
from Overlay import Overlay
from Paddle import Paddle

class Game():
    """Sets up the environment, all of the balls, bricks, paddle, etc.,
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

        self.__paddle = Paddle(self)

        self.__overlay = Overlay()

        self.__groupBricks = pg.sprite.RenderPlain()

        self.__groupBalls = pg.sprite.RenderPlain()

        self.__collidables = pg.sprite.Group()


        # Initializes the mixer.
        mixer.init()

        # Music by Alexander Nakarada, copyright free
        mixer.music.load("Space Ambience.mp3")
        mixer.music.set_volume(0.6)



    def run(self):   
        # Play music indefinitely
        mixer.music.play(-1)

        self.__addBall()

        # Loops through the x and y variables each brick will occupy.
        for x in range(0, int(self.__COLUMNS * self.__BRICK_WIDTH), int(self.__BRICK_WIDTH)):
            for y in range(0, int(self.__ROWS * self.__BRICK_HEIGHT), int(self.__BRICK_HEIGHT)):
                self.__addBrick(self.__BRICK_WIDTH, self.__BRICK_HEIGHT, x, y)

        self.__collidables.add(self.__paddle, self.__groupBricks.sprites())

        while self.__running:

            # Event handling.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__running = False
                
                # Secret key to add a ball.
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.__addBall()
                
            keys = pg.key.get_pressed()
            if  keys[pg.K_LEFT]:
                self.__paddle.moveLeft(self)
            if  keys[pg.K_RIGHT]:
                self.__paddle.moveRight(self)
                
                        

            # Object updating.
            self.__paddle.update()
            for ball in self.__balls:
                ball.update()
            for brick in self.__bricks:
                brick.update()
            self.__overlay.update()

            # Redrawing.
            self.__screen.fill((255,255,255))
            
            self.__paddle.draw(self.__screen)
            
            self.__groupBricks.draw(self.__screen)

            self.__groupBalls.draw(self.__screen)

            # for brick in self.__bricks:
            #     brick.draw(self.__screen)

            # for ball in self.__balls:
            #     ball.draw(self.__screen)

            self.__overlay.draw(self.__screen)

            pg.display.flip()
            self.__clock.tick(60)


        # Quit the game when no longer running.    
        pg.quit()

    def __addBall(self):
        """Adds a ball to the list of balls so that multiple
        may appear on the screen.
        """

        ball = Ball(self)
        self.__groupBalls.add(ball)
        self.__balls.append(ball)

    def __addBrick(self, width, height, x, y):
        """Adds a brick to the list of bricks so that multiple may
        appear on the screen.
        """

        brick = Brick(self, width, height, x, y)
        self.__groupBricks.add(brick)
        self.__bricks.append(brick)

    def getWidth(self):
        return self.__SCREEN_WIDTH

    def getHeight(self):
        return self.__SCREEN_HEIGHT

    def getCollidables(self):
        #return self.__groupBricks
        return self.__collidables

    def getBalls(self):
        return self.__groupBalls