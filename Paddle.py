import pygame as pg

class Paddle(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The paddle is a black rectangle. Can
    be moved left and right inside the bounds of the screen."""


    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)

        self.__size = 200

        self.__image = pg.Surface((self.__size, 10))

        self.__speed = 10


        # placeholder
        self.__rect = self.__image.get_rect()
        self.__rect.x = int(game.getWidth() / 2 - self.__size / 2)
        self.__rect.y = game.getHeight() - 20

    def draw(self, screen):
        """Draws the paddle to the screen."""
        screen.blit(self.__image, self.__rect)

    def update(self):
        pass

    def moveLeft(self, game):
        """Moves the paddle left."""

        if self.__rect.x >= 0:
            self.__rect.x = self.__rect.x - self.__speed

    def moveRight(self, game):
        """Moves the paddle right."""

        if self.__rect.x <= game.getWidth() - self.__size:
            self.__rect.x = self.__rect.x + self.__speed

    def __isValid(self, game):
        """Checks if a placement of the paddle is valid."""
        return self.__rect.x >= 0 and self.__rect.y <= game.getWidth() - self.__size


        