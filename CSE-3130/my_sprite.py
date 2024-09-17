import pygame

class mySprite:
    """
    Many of the common attributes and methods for sprites in pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR=(255, 255, 255)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # MODIFIER
    ###Movement Methods
    def marqueeX(self, MAX_WIDTH, MIN_WIDTH=0):
        self.__X += self.__SPD
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()

        self.__POS = (self.__X, self.__Y)
    def moveWASD(self, KEY_PRESSED):
        """
        move sprite with WASD
        :param KEY_PRESSED:  List
        :return: none
        """
        if KEY_PRESSED[pygame.K_d]:
            self.__X += self.__SPD
        if KEY_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD
        if KEY_PRESSED[pygame.K_w]:
            self.__Y -= self.__SPD
        if KEY_PRESSED[pygame.K_s]:
            self.__Y += self.__SPD
        self.__POS = (self.__X, self.__Y)
    def setWidth(self, WIDHT):
        self.__WIDTH = WIDHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    def getDimensions(self):
        return (self._SURFACE.get_width(), self._SURFACE.get_height())

    def setPos(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        self._COLOR = TUPLE

    def setSpeed(self, SPD):
        self.__SPD = SPD


    # ACCESSOR
    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getDim(self):
        return self._DIM

    def getPos(self):
        return self.__POS

    def getSurface(self):
        return self._SURFACE


    def isSpriteColliding(self, POSITION, DIMENSION):
        """
        Check if a sprite is colliding with the current sprite
        :param POSITION: tuple
        :param DIMENSION: tuple
        :return: bool
        """
        SPRITE_X = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]
        if SPRITE_X >= self.__X - SPRITE_W and SPRITE_X <= self.__X + self.getWidth():

                if SPRITE_Y >= self.__Y - SPRITE_H and SPRITE_Y <= self.__Y + self.getHeight():
                    return True

        return False





