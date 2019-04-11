import pygame
from window import Window
from game import Game
from Ball import Ball

pygame.init()


w = Window
ball = Ball(20)
g = Game()


if __name__ == "__main__":
    pygame.init()
    w(800, 600)
    g.run()