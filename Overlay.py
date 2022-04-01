import pygame as pg

class Overlay():
    """Overlay draws the score and number of lives."""
    

    def __init__(self):
        """Constructor."""

        # Creates the sprite.
        pg.sprite.Sprite.__init__(self)

        # Sets the font.
        self.__font = pg.font.SysFont(None, 30)

        # Sets the text.
        self.__text = self.__font.render("Temp", 1, (10, 10, 10))

        # Creates the rectangle for the sprite.
        self.__rect = self.__text.get_rect()

        # Sets the position on screen.
        self.__rect.x = 2
        self.__rect.y = 2

        # Sets the initial lives and score.
        self.__lives = 3
        self.__score = 0


    def draw(self, screen):
        """Draws the lives and score on the screen."""

        # Sets the text to be displayed.
        self.__text = self.__font.render("Score: " + str(self.__score) + 
                                  "       Lives: " + str(self.__lives), 1, (10, 10, 10))

        # Displays the text.
        screen.blit(self.__text, self.__rect)


    def update():
        """Updates the Overlay object."""


    def setLives(self, lives):
        """Sets the number of lives the player has."""
        self.__lives = lives


    def setScore(self, score):
        """Sets the score of the game."""
        self.__score = score


    def getLives(self):
        """Gets the amount of lives the player has."""
        return self.__lives


    def getScore(self):
        """Gets the score of the game."""
        return self.__score