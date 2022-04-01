import pygame as pg

class Paddle(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The padde is a black rectangle. Can
    be moved left and right inside the bounds of the screen."""

    __speed__ = -1

    __size__ = -1

    def draw(self, screen):
        pass

    def update(self):
        pass