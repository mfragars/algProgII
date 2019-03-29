"""Classe Windows"""

import pygame

class Window(object):
    """Implementa objeto de janela usando PYGame"""
    def __init__(self):
        """Inicializa objeto window"""
        self._width , self._heigth = size = (800, 600)
        self._title = "Oi, sou o PyGame"
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self._title)

    def update(self):
        pygame.display.update()

    def draw(self, object):
        pygame.draw.circle(_screen, (0, 255, 0), object)
            

