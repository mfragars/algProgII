import pygame

pygame.init()
(width, heigth) = (800, 600)
window_title = "Oi, sou o PyGame"

screen = pygame.display.set_mode((width, heigth))

pygame.display.set_caption(window_title)
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()


