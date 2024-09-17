# my_sprite.py in d_inheritance

"""
title: Abstract sprite class
author: Austin Meng
date-created: 2023-04-14
"""
import pygame
class mySprite():
    """
    Many of the common attributes and methods for sprites in pygame
    """
    def __init__(self):
        self.__HEIGHT = 0
        self.__WIDTH = 0
        self._SURFACE = pygame.Surface
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)
        self.__DIM = (self.__WIDTH, self.__HEIGHT)
        self.__SPD = 0
        self._COLOR = (255,255,255) #white
        self.__DIR_X = 1
        self.__DIR_Y = 1


    # Modifier methods
    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self.__DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)

    def setPosition(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)
    def setColor(self, TUPLE):
        self._COLOR = TUPLE

    #accessor methods
    def getWidth(self):
        return self._SURFACE.get_width()
    def getHeight(self):
        return self._SURFACE.get_height()

    def getPOS(self):
        return self.__POS
    def getSurface(self):
        return self._SURFACE

    def getDimensions(self):
        return self.__DIM