import random
import pygame as pg
from pygame import mixer



class Brick(pg.sprite.Sprite): 
    """Subclass of pg.sprite.Sprite. A brick has a randomly chosen
    color. The health of the brick is calculated by summing the values
    of each RGB value. Each time the brick is hit, 25 health is removed.
    """

    def __init__(self, game, width, height, x, y):
        """Constructor. Sets the size, position, random color, and 
        health of the brick.
        """

        # Create the sprite.
        pg.sprite.Sprite.__init__(self)

        # The surface of the brick.
        self.image = pg.Surface((width, height))

        # The game the brick is in.
        self.__game = game

        # Chooses a random color for the brick.
        self.__r = random.randint(0,255)
        self.__g = random.randint(0,255)
        self.__b = random.randint(0,255)

        # Determines the health from each color value.
        self.__health = self.__r + self.__g + self.__b

        # Colors the brick.
        self.image.fill( (self.__r, self.__g, self.__b) )

        # The position of the brick on the screen.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """Draws the brick to the screen."""
        screen.blit(self.image, self.rect)

    def hit(self):
        """Removes 50 health from the brick and kills it if less or 
        equal to 0.
        """

        self.__health = self.__health - 50

        if self.__health <= 0:
            # https://freesound.org/people/LittleRobotSoundFactory/sounds/270327/
            # Created by LittleRobotSoundFactory, no modifications.
            pg.mixer.Sound.play(pg.mixer.Sound("Hit.wav"))

            # Removes the brick from its group and increase the score.
            self.kill()
            score = self.__game.getOverlay().getScore() + 50
            self.__game.getOverlay().setScore(score)