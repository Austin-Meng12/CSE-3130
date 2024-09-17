# c_startfield.py

"""

title: starfield examples
author: Austin Meng
date-created: 2023-04-13
"""

if __name__ == "__main__":
    import pygame
    from a_template import Window
    from b_boxes import Box
    import random

    WINDOW = Window("Starfield")

    STARS = []
    for i in range(100):
        STAR_SIZE = random.randrange(1,6)
        STARS.append(Box(STAR_SIZE, STAR_SIZE, random.randint(0, WINDOW.getWidth() - STAR_SIZE), random.randint(0, WINDOW.getWidth() - STAR_SIZE) ))

    PLAYER = Box(50, 50, WINDOW.getWidth()//2 - 50//2, WINDOW.getHeight()//2 - 50//2)


    while True:
        #INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # processing

        PRESSED_KEYS = pygame.key.get_pressed()

        for star in STARS:

            star.moveBox(PRESSED_KEYS)

            star.wrapBox(WINDOW.getWidth(), WINDOW.getHeight())
            #star.scrollX(WINDOW.getWidth())
        #PLAYER.moveBox(PRESSED_KEYS)
        #PLAYER.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())

        #output
        WINDOW.clearScreen()
        for star in STARS:
            WINDOW.getSurface().blit(star.getSurface(), star.getPOS())
            WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()

