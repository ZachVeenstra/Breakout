import random
import pygame as pg


class Brick(pg.sprite.Sprite): 
    """Subclass of pg.sprite.Sprite. A brick has a randomly chosen
    color. The health of the brick is calculated by summing the values
    of each RGB value. Each time the brick is hit, 25 health is removed."""

    def __init__(self, width, height, x, y):
        pg.sprite.Sprite.__init__(self)

        self.__image = pg.Surface((width, height))


        self.__r = random.randint(0,255)
        self.__g = random.randint(0,255)
        self.__b = random.randint(0,255)

        self.__health = self.__r + self.__g + self.__b

        self.__image.fill( (self.__r, self.__g, self.__b) )
        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y

    def draw(self, screen):
        screen.blit(self.__image, self.__rect)

    def update(self):
        pass

    def hit(self):
        self.__health = self.__health - 25
        if self.__health <= 0:
            self.kill()