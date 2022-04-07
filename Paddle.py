import pygame as pg

class Paddle(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The padde is a black rectangle. Can
    be moved left and right inside the bounds of the screen."""


    def __init__(self,):
        pg.sprite.Sprite.__init__(self)

        self.__size = 200

        self.__image = pg.Surface((self.__size, 10))

        self.__speed = 1


        # placeholder
        self.__rect = self.__image.get_rect()
        self.__rect.x = 300
        self.__rect.y = 580

    def draw(self, screen):
        """Draws the paddle to the screen."""
        screen.blit(self.__image, self.__rect)

    def update(self):
        pass

    def moveLeft(self):
        """Moves the paddle left."""

        self.__rect.x = self.__rect.x - self.__speed

    def moveRight(self):
        """Moves the paddle right."""

        self.__rect.x = self.__rect.x + self.__speed