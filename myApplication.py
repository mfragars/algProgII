"""Executa a abertura da Janela"""

import pygame
from window import Window
from application import Application

if __name__ == "__main__":
    pygame.init()
    Window()
    Application().run()