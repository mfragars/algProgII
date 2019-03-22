"""Classe Aplicação"""
import pygame

class Application:
    """Implementa uma aplicação"""
    def __init__(self):
        """Inicializa a janela"""
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False