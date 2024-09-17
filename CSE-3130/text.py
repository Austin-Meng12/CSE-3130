import pygame
from window import Window
from my_sprite import mySprite

class Text(mySprite):
    """
    Concrete text sprite
    """
    def __init__(self, TEXT):
        mySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT = pygame.font.SysFont("Arial", 36)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    # MODIFIER
    def setColor(self, TUPLE):
        # polymorphs the setColor class from mySprite
        mySprite.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Text Title")
    TEXT = Text("Hello World")
    TEXT.setColor((0, 255, 0))
    TEXT.setSpeed(10)

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # PROCESSING
        TEXT.marqueeX(WINDOW.getWidth())

        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPos())
        WINDOW.updateFrame()