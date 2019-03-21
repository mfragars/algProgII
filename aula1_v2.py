"""Classe Windows"""

import pygame

class window(object):
        """Implementa objeto de janela usando PYGame"""
        def __init__(self):
            """Inicializa objeto window"""
            self._width , self._heigth = size = (800, 600)
            self._title = "Oi, sou o PyGame"
            pygame.display.set_mode(size)
            pygame.display.set_caption(self._title)

if __name__ == "__main__":
    janela = window()