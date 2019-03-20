import pygame

class janela(object):
        width=800
        heigth=600
        title="Oi, sou o PyGame" 


def main():

    pygame.init()
    screen = pygame.display.set_mode((janela.width, janela.heigth))
    pygame.display.set_caption(janela.title)
    done = False

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            
            pygame.display.flip()
if __name__== "__main__":
  main()