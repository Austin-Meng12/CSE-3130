import pygame

class Window:
    """
    Create the window that will load the game
    :return: None
    """
    def __init__(self, TITLE, WIDTH = 800, HEIGHT=600, FPS=30):
        self. __TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__BG_COLOR = (50, 50, 50)
        self.__FRAME = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM) # Surface object in pygame. Every item in your program will overlay on top of a surface object.
        self.__SURFACE.fill(self.__BG_COLOR)
        pygame.display.set_caption(self.__TITLE)


    ## MODIFIER METHODS
    def updateFrame(self):
        """
        Update the window object based on FPS
        :return:
        """
        self.__FRAME.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        """
        Fill screen with bg color
        :return:
        """
        self.__SURFACE.fill(self.__BG_COLOR)

    ## ACCESSOR
    def getSurface(self):
        return self.__SURFACE
    def getWidth(self):
        return self.__WIDTH
    def getHeight(self):
        return self.__HEIGHT