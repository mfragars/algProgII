"""Classe Aplicação"""
import pygame

class Application:
    """Implementa uma aplicação"""
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running
            event == pygame.event.get()
            if event == pygame.QUIT:
                self.running = False
            
