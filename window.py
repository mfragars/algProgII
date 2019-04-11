"""Classe Windows"""

import pygame

class Window(object):
    """Implementa objeto de janela usando PYGame"""
    def __init__(self, width, heigth):
        """Inicializa objeto window"""
        
        self._width , self._heigth = size = (width, heigth)
        self.__title = "Oi, sou o PyGame"
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.__title)

    def update(self):
        pygame.display.update()
            
    @property
    def width(self):
        """Return the width of the window."""
        return self._width

    @property
    def height(self):
        """Return the height of the window."""
        return self._heigth    