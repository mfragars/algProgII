"""Classe Aplicação"""
import pygame
from window import Window
from Ball import Ball

w = Window()
ball = Ball(20)

class Application:
    """Implementa uma aplicação"""
    def __init__(self):
        """Inicializa a janela"""
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            w.draw(ball)
            w.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    