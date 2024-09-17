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
        self.__FONT = pygame.font.SysFont("arial",36)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)
