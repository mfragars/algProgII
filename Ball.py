"""Classe Ball"""

import pygame


class Ball():
    """Implementa Objeto Bola utilizando PyGame Sprite"""
    def __init__(self, r):
        self.x = 0
        self.y = 0
        self.r = r

    @property
    def position(self):
        return (self.x, self.y)
        
    @position.setter
    def position(self, position):
        self.x, self.y = position

    def move(self, dx, dy):
        self.x += dx
        self.y += dy