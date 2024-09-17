'''
Title: Pygame Template
Author: Dominic Khorrami-Arani
Date-created: 2023-04-11
'''

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

class Text:
    """
    Creates a text object to be placed on a surface
    """
    def __init__(self, TEXT):
        self.__TEXT = TEXT
        self.__COLOR = (255, 255, 255)  # RGB value of White
        self.__FONT = pygame.font.SysFont("IMPACT", 36)
        self.__SURFACE = self.__FONT.render(self.__TEXT, True, self.__COLOR)
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)
        self.__SPD = 5
        self.__DIR_X = 1
        self.__DIR_Y = 1
    # MODIFIER METHODS
    def setPOS(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)
    def setColor(self,TUPLE):
        self.__COLOR = TUPLE
        self.__SURFACE = self.__FONT.render(self.__TEXT, True, self.__COLOR)
    def marqueeX(self, SCREEN_WIDTH):
        """
        Object move left to right and wrap around the screen
        :return:
        """
        if self.__X > SCREEN_WIDTH:
            self.__X = 0 - self.getWidth()
        else:
            self.__X += 5
        self.__POS = (self.__X, self.__Y)
    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN = 0):
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__DIR_X = -1
        elif self.__X < SCREEN_WIDTH_MIN:
            self.__DIR_X = 1

        self.__POS = (self.__X, self.__Y)


    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN = 0):
        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self.__DIR_Y = -1
        elif self.__Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 1
        self.__POS = (self.__X, self.__Y)
    # ACCESSOR METHODS
    def getPOS(self):
        return self.__POS

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()




if __name__ == "__main__":
    # Main program code
    pygame.init()
    # Create window
    WINDOW = Window("template", 800, 600, 30)
    # Create text object
    TEXT = Text("hello world")
    TEXT.setPOS((WINDOW.getWidth()//2, WINDOW.getHeight()//2 - TEXT.getHeight()//2))
    # Do loop similar to AGK
    TEXT.setColor((0,255,8))


    while True:
        #### INPUTS
        # Allow the X in the title bar to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #### PROCESSING
        #TEXT.marqueeX(WINDOW.getWidth())
        TEXT.bounceY(WINDOW.getHeight())
        TEXT.bounceX(WINDOW.getWidth())

        #### OUTPUTS
        WINDOW.clearScreen()  # Text is cleared so that it does not get left behind
        # Get screen of window and smack on text
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())

        WINDOW.updateFrame()  # Like sync function in AGK.