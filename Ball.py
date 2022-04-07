import pygame as pg

class Ball(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The ball will bounce off walls, the
    paddle, and bricks."""

    def __init__(self):
        """Constructor"""
        pg.sprite.Sprite.__init__(self)
        self.__image = pg.Surface((10, 10))

        # Placeholder
        self.__rect = self.__image.get_rect()
        self.__rect.x = 700
        self.__rect.y = 300

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    def update(self):
        pass