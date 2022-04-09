import pygame as pg
from pygame import mixer

class Ball(pg.sprite.Sprite):
    """Subclass of pg.sprite.Sprite. The ball will bounce off walls, the
    paddle, and bricks."""

    def __init__(self, game):
        """Constructor"""
        pg.sprite.Sprite.__init__(self)

        # self.__hitSound = pg.mixer.Sound("")

        self.__size = 10

        self.image = pg.Surface((self.__size, self.__size))

        self.__game = game

        self.__speed = 3

        self.__velocity = { "x-speed": self.__speed, 
                            "y-speed": self.__speed
                          }

        # Placeholder
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ball."""
        if(pg.sprite.spritecollideany(self, self.__game.getCollidables()) or
           self.rect.y <= 0):
            self.__velocity["y-speed"] = self.__velocity["y-speed"] * -1
        
        if(self.rect.x <= 0 or self.rect.x >= self.__game.getWidth() - self.__size):
            self.__velocity["x-speed"] = self.__velocity["x-speed"] * -1

        self.rect.x = self.rect.x + self.__velocity["x-speed"]
        self.rect.y = self.rect.y + self.__velocity["y-speed"]