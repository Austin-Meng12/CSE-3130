# image_sprite.py in e_bunny directory

"""
Title: Image Sprite
Author: Austin Meng
date-created: 2023-04-19
"""

import pygame
from my_sprite import mySprite

class ImageSprite(mySprite):
    """
    load and manipulate images

    """
    def __init__(self, IMAGE_FILE):


        mySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__X_FLIP = False


    #Modifier Methods


    ###Movement
    def moveWASD(self, KEY_PRESSED):
        mySprite.moveWASD(self, KEY_PRESSED)
        if KEY_PRESSED[pygame.K_d]:
            if  not self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = True
        if KEY_PRESSED[pygame.K_a]:
            if self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = False

    ###Properties
    def setScale(self, SCALE_X, SCALE_Y = 0):
        """
        Resize the image based on a factor
        :param SCALE_X: float
        :param SCALE_Y: float
        :return:
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE,
                    (self.getWidth() * SCALE_X, self.getHeight() * SCALE_Y))
    def setFlipX(self):
        """
        Flip the image on the y-axis

        :return: none

        """

        self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Image sprite test")
    BUNNY = ImageSprite("images/bunny.png")
    BUNNY.setScale(0.6)
    BUNNY.setSpeed(10)
    BUNNY.setFlipX()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Processing
        PRESSED_KEYS = pygame.key.get_pressed()
        BUNNY.moveWASD(PRESSED_KEYS)

        #OUTPUT
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BUNNY.getSurface(), BUNNY.getPos())
        WINDOW.updateFrame()
