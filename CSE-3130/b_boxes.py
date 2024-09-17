# b_boxes.py
'''
title: box class for pygame
author: Austin Meng
date-created: 2023-04-12

'''
import pygame

from a_template import Window

class Box:
    """
    Creates a box object in pygame

    """

    def __init__(self, WIDTH = 1, HEIGHT = 1, X =0, Y =0):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__COLOR = (255,255,255) # white
        self.__SURFACE = pygame.Surface(self.__DIM, pygame.SRCALPHA, 32)
        self.__SURFACE.fill(self.__COLOR)
        self.__SPD = 10

    # mutator
    def setPOS(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    def moveBox(self, KEYS_PRESSED):
        """
        Move the box with WASD


        :param KEYS_PRESSED:
        :return:
        """

        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD
        if KEYS_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD
        if KEYS_PRESSED[pygame.K_w]:
            self.__Y -= self.__SPD
        if KEYS_PRESSED[pygame.K_s]:
            self.__Y += self.__SPD
        self.__POS = (self.__X, self.__Y)


    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X = 0, MIN_Y=0):
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y


        self.__POS = (self.__X, self.__Y)
    def wrapBox(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT = 0):
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()
        if self.__X < MIN_WIDTH - self.getWidth():
            self.__X = MAX_WIDTH
        if self.__Y > MAX_HEIGHT:
            self.__Y = MIN_HEIGHT - self.getHeight()
        if self.__Y < MIN_HEIGHT - self.getHeight():
            self.__Y = MAX_HEIGHT

        self.__POS = (self.__X, self.__Y)


    def scrollX(self, MAX_WIDTH, MIN_WIDTH = 0):
        self.__X -= self.__SPD
        if self.__X < MIN_WIDTH - self.getWidth():
            self.__X = MAX_WIDTH
        self.__POS = (self.__X, self.__Y)



    # accessor methods
    def getSurface(self):
        return self.__SURFACE


    def getPOS(self):
        return self.__POS


    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("BOXES", 800, 600, 30)
    BOX = Box(100, 100)
    BOX.setPOS((WINDOW.getWidth()//2 - BOX.getWidth()//2, WINDOW.getHeight()//2 - BOX.getHeight()//2))

    while True:
        #input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()




        # Processing

        BOX.moveBox(PRESSED_KEYS)
        BOX.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())

        #Output
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPOS())
        WINDOW.updateFrame()


