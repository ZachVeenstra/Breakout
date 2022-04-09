import random
import pygame as pg



class Brick(pg.sprite.Sprite): 
    """Subclass of pg.sprite.Sprite. A brick has a randomly chosen
    color. The health of the brick is calculated by summing the values
    of each RGB value. Each time the brick is hit, 25 health is removed."""

    def __init__(self, game, width, height, x, y):
        pg.sprite.Sprite.__init__(self)


        self.image = pg.Surface((width, height))

        self.__game = game

        self.__r = random.randint(0,255)
        self.__g = random.randint(0,255)
        self.__b = random.randint(0,255)

        self.__health = self.__r + self.__g + self.__b

        self.image.fill( (self.__r, self.__g, self.__b) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if (pg.sprite.spritecollideany(self, self.__game.getBalls())):
            self.hit()

    def hit(self):
        self.__health = self.__health - 25
        if self.__health <= 0:
            self.kill()