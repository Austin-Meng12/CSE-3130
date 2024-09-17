# text.py in d_inheritance

'''
title: Text Class
author: Austin Meng
date-created: 2023-04-14
'''
import pygame
from my_sprite import mySprite
class Text(mySprite):
    """
    Concrete text sprite
    """

    def __init__(self, TEXT):
        mySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_SIZE = 36
        self.__FONT = pygame.font.SysFont("arial",self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)




    def setColor(self, TUPLE):
        #polymorphs the setColor class from mySprite
        mySprite.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setFontSize(self, NEW_SIZE):
        self.__FONT_SIZE = NEW_SIZE
        self.__FONT = pygame.font.SysFont("Arial", self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)