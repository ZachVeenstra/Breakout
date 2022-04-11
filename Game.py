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
        """Constructor creates the screen, sets the amount of bricks
        that appear, creates a time clock, creates groups of bricks, 
        balls, a paddle and an overlay.
        """
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

        # The clock determines how many updates to the screen there are
        # per second
        self.__clock = pg.time.Clock()

        # The current game state.
        self.__running = True

        # Displays the current score and lives.
        self.__overlay = Overlay()

        # The paddle.
        self.__paddle = Paddle(self)

        # These are all in groups, which allow them to more easily be
        # drawn to the screen and provides simpler collision detection.
        self.__groupBricks = pg.sprite.RenderPlain()

        self.__groupBalls = pg.sprite.RenderPlain()

        self.__collidables = pg.sprite.Group()

        # Initializes the mixer which allows the background music to be
        # played.
        mixer.init()

        # Music by Alexander Nakarada, copyright free
        mixer.music.load("Space Ambience.mp3")
        mixer.music.set_volume(0.6)


    def run(self):
        """Creates all of the brick objects first, then runs the game 
        loop. During the game loop, keyboard input is taken, moving 
        objects are updated, objects are redrawn, and game state is
        checked.
        """
        # Play music indefinitely
        mixer.music.play(-1)

        # This is the initial ball
        self.addBall()

        # Loops through the x and y variables each brick will occupy and
        # adds a brick to the specified location.
        for x in range(0, int(self.__COLUMNS * self.__BRICK_WIDTH), int(self.__BRICK_WIDTH)):
            for y in range(0, int(self.__ROWS * self.__BRICK_HEIGHT), int(self.__BRICK_HEIGHT)):
                self.__addBrick(self.__BRICK_WIDTH, self.__BRICK_HEIGHT, x, y)

        # This group specifies which objects can collide with the ball.
        self.getCollidables().add(self.__paddle, self.__groupBricks.sprites())

        # This is the game loop.
        while self.__running:

            # Event handling.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__running = False
                
                # Secret key to add a ball.
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.addBall()
                
            # Detects the arrow keys to move the paddle.    
            keys = pg.key.get_pressed()
            if  keys[pg.K_LEFT]:
                self.getPaddle().moveLeft()
            if  keys[pg.K_RIGHT]:
                self.getPaddle().moveRight()
                

            # Object updating.
            for ball in self.getBalls().sprites():
                ball.update()


            # Redrawing.
            self.__screen.fill((255,255,255))
            
            self.__paddle.draw(self.__screen)
            
            self.getBricks().draw(self.__screen)

            self.getBalls().draw(self.__screen)

            self.__overlay.draw(self.__screen)

            pg.display.flip()


            # Updates the screen at 60 fps.
            self.__clock.tick(60)


            # Checks for win or loss.
            if len(self.getBricks().sprites()) == 0:
                print ("YOU WIN!")
                self.__running = False
            
            if self.getOverlay().getLives() == 0:
                self.__running = False


        # Quit the game when no longer running.    
        pg.quit()


    def addBall(self):
        """Adds a ball to the list of balls so that multiple
        may appear on the screen.
        """

        ball = Ball(self)
        self.getBalls().add(ball)


    def __addBrick(self, width, height, x, y):
        """Adds a brick to the list of bricks so that multiple may
        appear on the screen.
        """

        brick = Brick(self, width, height, x, y)
        self.__groupBricks.add(brick)


    def getWidth(self):
        """Gets the width of the screen in pixels."""
        return self.__SCREEN_WIDTH


    def getHeight(self):
        """Gets the height of the screen in pixels."""
        return self.__SCREEN_HEIGHT


    def getCollidables(self):
        """Gets the sprites that can be collided with."""
        return self.__collidables


    def getBalls(self):
        """Gets the group of balls."""
        return self.__groupBalls


    def getOverlay(self):
        """Gets the overlay of the lives and score."""
        return self.__overlay


    def getBricks(self):
        """Gets the group of bricks."""
        return self.__groupBricks


    def getPaddle(self):
        """Gets the paddle."""
        return self.__paddle