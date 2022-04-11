import pygame as pg
from pygame import mixer

from Brick import Brick

class Ball(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The ball will bounce off walls, the
    paddle, and bricks."""

    def __init__(self, game):
        """Constructor. Sets the SIZE and SPEED of the ball, and sets
        the initial position and velocity.
        """

        # Creates the sprite.
        pg.sprite.Sprite.__init__(self)

        # Meaured in pixels.
        self.__SIZE = 10

        # Can move 3 pixels per frame.
        self.__SPEED = 3

        # The suface is a square as big as the size of the ball.
        self.image = pg.Surface((self.__SIZE, self.__SIZE))

        # The game the ball is in.
        self.__game = game

        # Determines the speed in the x and y directions.
        self.__velocity = { "x-speed": self.__SPEED, 
                            "y-speed": self.__SPEED
                          }

        # The ball will start off in the center of the screen.
        self.rect = self.image.get_rect()
        self.rect.x = self.__game.getWidth() / 2
        self.rect.y = self.__game.getHeight() / 2 + 1 # 1 pixel off of the bricks starting position


    def draw(self, screen):
        """Draws the ball to the screen."""
        screen.blit(self.image, self.rect)

    def update(self):
        """Detects collisions with the paddle, the bricks and the edges 
        of the screen. If the ball hits a brick, it calls that brick's
        hit method in order to deal damage.
        """

        # If the ball hits a brick or the paddle.
        if(pg.sprite.spritecollideany(self, self.__game.getCollidables()) or
           self.rect.y <= 0):

            # If it hit a brick, damage it.
            if type(pg.sprite.spritecollideany(self, self.__game.getCollidables()))  == Brick:
                pg.sprite.spritecollideany(self, self.__game.getCollidables()).hit()

            # Copyright-free sound.
            pg.mixer.Sound.play(pg.mixer.Sound("Bounce.wav"))

            # Invert the velecity in the y direction.
            # Small bug if the ball hits the side of a brick or paddle,
            # it should invert the x velocity, but there's no good way 
            # to check for that with the built-in methods.
            self.__velocity["y-speed"] = self.__velocity["y-speed"] * -1
        

        # If the ball hits the side of the screen, make it bounce.
        if(self.rect.x <= 0 or self.rect.x >= self.__game.getWidth() - self.__SIZE):
            self.__velocity["x-speed"] = self.__velocity["x-speed"] * -1

        # If the ball goes off the bottom of the screen, remove it from
        # the ball group and subtract a life..
        if(self.rect.y == self.__game.getHeight() + 1):
            lives = self.__game.getOverlay().getLives()
            self.kill()
            if lives > 0:
                self.__game.getOverlay().setLives(lives - 1)
                self.__game.addBall()

        # Update the x and y position of the ball.
        self.rect.x = self.rect.x + self.__velocity["x-speed"]
        self.rect.y = self.rect.y + self.__velocity["y-speed"]