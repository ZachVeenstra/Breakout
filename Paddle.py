import pygame as pg

class Paddle(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The paddle is a black rectangle. Can
    be moved left and right inside the bounds of the screen."""


    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)

        self.__size = 200

        self.image = pg.Surface((self.__size, 10))

        self.__speed = 6


        # placeholder
        self.rect = self.image.get_rect()
        self.rect.x = int(game.getWidth() / 2 - self.__size / 2)
        self.rect.y = game.getHeight() - 20

    def draw(self, screen):
        """Draws the paddle to the screen."""
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def moveLeft(self, game):
        """Moves the paddle left."""

        if self.rect.x >= 0:
            self.rect.x = self.rect.x - self.__speed

    def moveRight(self, game):
        """Moves the paddle right."""

        if self.rect.x <= game.getWidth() - self.__size:
            self.rect.x = self.rect.x + self.__speed

    def __isValid(self, game):
        """Checks if a placement of the paddle is valid."""
        return self.rect.x >= 0 and self.rect.y <= game.getWidth() - self.__size


        