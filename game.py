
import pygame
from window import Window
from Ball import Ball

w = Window(800, 600)
ball = Ball(10)


class Game:
    def __init__(self):
        self.running = False
        self.x = 400
        self.y = 300
        

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update()
            self.draw()
            pygame.display.update()


    def draw(self):
        pygame.draw.circle(w.screen, (0, 255,0), (self.x,self.y), ball.r)
    
    def update(self):
        if self.x <= w._heigth-ball.r and self.x > ball.r:
            self.x += 1
            self.y += 1
        elif self.x == w._heigth-ball.r and self.y <= w._width-ball.r:
            self.x -= 1
            self.y += 1
        

        ball.move(self.x, self.y)