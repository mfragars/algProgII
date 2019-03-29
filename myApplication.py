"""Executa a abertura da Janela"""

import pygame
from window import Window
from application import Application
from Ball import Ball

if __name__ == "__main__":
    pygame.init()
    Ball.position = (400,300)
    Application().run()