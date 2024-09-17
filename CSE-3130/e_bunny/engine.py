# engine.py in e_bunny directory

"""
title: Egg hunt game engine
author: Austin Meng
date-created: 2023-04-19
"""
import pygame
from text import Text
from image_sprite import ImageSprite
from window import Window
import random

class Engine:

    def __init__(self):
        self.__WINDOW = Window("Egg Hunt")
        self.__TITLE = Text("Egg Hunt")

        self.__TITLE.setPos((self.__WINDOW.getWidth() // 2 - self.__TITLE.getWidth() // 2, 0))
        self.__PLAYER = ImageSprite("images/shrek.png")
        self.__PLAYER.setScale(0.5)

        self.__PLAYER.setPos(
            (
                self.__WINDOW.getWidth()//2 - self.__PLAYER.getWidth()//2,
                self.__WINDOW.getHeight()//2 - self.__PLAYER.getHeight()//2


            )

        )
        self.__PLAYER.setSpeed(10)

        self.__EGG = [
                ImageSprite("images/red.png"),
                ImageSprite("images/red.png")
        ]
        for egg in self.__EGG:
            egg.setScale(0.5)
            egg.setPos((
                random.randrange(self.__WINDOW.getWidth() - egg.getWidth()),
                random.randrange(self.__TITLE.getHeight(), self.__WINDOW.getHeight() - egg.getHeight())

            ))

        self.__SHRUB = [
            ImageSprite("images/shrek_toliet.png"),
            ImageSprite("images/shrek_toliet.png")
        ]
        for shrub in self.__SHRUB:
            shrub.setScale(0.1)
            shrub.setPos((
                random.randrange(self.__WINDOW.getWidth() - shrub.getWidth()),
                random.randrange(self.__TITLE.getHeight(), self.__WINDOW.getHeight() - shrub.getHeight())
            ))


        self.__BG_IMAGE = ImageSprite("images/league_map.png.jfif")
        self.__BG_IMAGE.setScale(4)
        self.__BG_IMAGE.setPos(
            (
                0,
                self.__TITLE.getHeight()
            )
        )



        self.__SCORE_VALUE = 0
        self.__SCORE_TEXT = Text(f"SCORE:{self.__SCORE_VALUE}")
        self.__SCORE_TEXT.setPos((self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 0))
        self.__WINNING_TEXT = Text("You Win")
        self.__WINNING_TEXT.setFontSize(196)
        self.__WINNING_TEXT.setPos((
            self.__WINDOW.getWidth(),
            self.__WINNING_TEXT.getHeight()
        )


        )


    def run(self):
        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            ### processing
            PRESSED_KEYS = pygame.key.get_pressed()
            self.__PLAYER.moveWASD(PRESSED_KEYS)
            self.__PLAYER.checkBoundaries(
                self.__WINDOW.getWidth() ,
                self.__WINDOW.getHeight() ,
                0,
                self.__TITLE.getHeight()
                )
            if self.__SHRUB[0].isSpriteColliding(self.__SHRUB[1].getPos(), self.__SHRUB[1].getDimensions()):
                self.__SHRUB[0].setPos(
                    (
                        random.randrange(self.__WINDOW.getWidth() - self.__SHRUB[0].getWidth()),
                        random.randrange(self.__TITLE.getHeight(),
                                         self.__WINDOW.getHeight() - self.__SHRUB[0].getWidth())

                    )
                )

            for egg in self.__EGG:

                if self.__PLAYER.isSpriteColliding(egg.getPos(), egg.getDimensions()):
                    egg.setPos(
                        (
                            random.randrange(self.__WINDOW.getWidth() - egg.getWidth()),
                            random.randrange(self.__TITLE.getHeight(), self.__WINDOW.getHeight()-egg.getWidth())

                        )

                    )
                    self.__SCORE_VALUE += 1
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPos(
                        (
                            self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 0
                        )

                    )
            if self.__SCORE_VALUE > 10:
                self.__setWinningScreen()
            ###outputs
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPos())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPos())
            for egg in self.__EGG:
                self.__WINDOW.getSurface().blit(egg.getSurface(), egg.getPos())
            for shrub in self.__SHRUB:
                self.__WINDOW.getSurface().blit(shrub.getSurface(), shrub.getPos())

            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPos())
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPos())
            self.__WINDOW.getSurface().blit(self.__WINNING_TEXT.getSurface(), self.__WINNING_TEXT.getPos())
            self.__WINDOW.updateFrame()

    def __setWinningScreen(self):
        self.__PLAYER.setPos((
            self.__WINDOW.getWidth(),
            self.__WINDOW.getHeight()


        ))
        for egg in self.__EGG:
            egg.setPos((
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
            )
        self.__SCORE_TEXT.setPos((
            self.__WINDOW.getWidth(),
            self.__WINDOW.getHeight()

        ))
        self.__WINNING_TEXT.setPos((
            self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2,
            self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2

        ))



if __name__ == "__main__":
    pygame.init()
    GAME = Engine()
    GAME.run()