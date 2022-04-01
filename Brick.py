import random
import pygame as pg


class Brick(pg.sprite.Sprite): 
    """Subclass of pg.sprite.Sprite. A brick has a randomly chosen
    color. The health of the brick is calculated by summing the values
    of each RGB value. Each time the brick is hit, 25 health is removed."""

    __health__ = 0

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((200, 200))


        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        __health__ = r + g + b

        self.image.fill( (r, g, b) )
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass

    def hit(self):
        pass