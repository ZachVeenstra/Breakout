import pygame as pg

class Paddle(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The paddle is a black rectangle. Can
    be moved left and right inside the bounds of the screen."""


    def __init__(self, game):
        """Constructor. Sets the size of the paddle, its speed, and
        initial position.
        """

        pg.sprite.Sprite.__init__(self)

        # Measured in pixels.
        self.__SIZE = 200

        # Can move six pixels per frame.
        self.__SPEED = 6

        # The surface is the size of the paddle wide and 10 pixels tall.
        self.image = pg.Surface((self.__SIZE, 10))

        # The game the paddle is in.
        self.__game = game

        # The Initial position of the paddle is in the center of the 
        # bottom of the screen.
        self.rect = self.image.get_rect()
        self.rect.x = int(self.__game.getWidth() / 2 - self.__SIZE / 2)
        self.rect.y = self.__game.getHeight() - 20


    def draw(self, screen):
        """Draws the paddle to the screen."""

        screen.blit(self.image, self.rect)


    def moveLeft(self):
        """Moves the paddle left if it isn't off the screen."""

        if self.rect.x >= 0:
            self.rect.x = self.rect.x - self.__SPEED


    def moveRight(self):
        """Moves the paddle right if it isn't off the screen"""

        if self.rect.x <= self.__game.getWidth() - self.__SIZE:
            self.rect.x = self.rect.x + self.__SPEED

        