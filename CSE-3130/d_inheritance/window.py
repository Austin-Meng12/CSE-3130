"""
title: window class
author: austin Meng
date-created: 2023-04-14


"""
import pygame

class Window:
    """
    Create the window that will load the game
    :return: None
    """
    def __init__(self, TITLE, WIDTH = 800, HEIGHT = 600, FPS = 30):
        self.__TITLE = TITLE  # Text that appears in the title bar.
        self.__FPS = FPS  # the frames per second the window will refresh
        self.__WIDTH = WIDTH  # width of the window
        self.__HEIGHT = HEIGHT  # height of the window
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__BG_COLOR = (50, 50, 50)  # uses the format (R, G, B)
        self.__FRAME = pygame.time.Clock()  # using clock object to determine how many frames should appear per second
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)  # Surface object in pygame. Every item in your program will overlay on top of a surface object.
        self.__SURFACE.fill(self.__BG_COLOR)



        pygame.display.set_caption(self.__TITLE)  # updates the title of the window to the title text.


    # MODIFIER METHODS
    def updateFrame(self):
        """
        Updating the Window object based on the FPS
        :return:
        """
        self.__FRAME.tick(self.__FPS)  # Waits for the appropriate time based on the set FPS  (Clock please wait for the appropriate time to be set in view
        pygame.display.flip()  # Updates the window with the new frame.

    def clearScreen(self):  # Run in the background so it can start again
        """
        Fill the screen with the background color
        :return:
        """
        self.__SURFACE.fill(self.__BG_COLOR)


    # ACCESSOR METHODS
    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT