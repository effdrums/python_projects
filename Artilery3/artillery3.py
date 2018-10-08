import pygame
import menu 


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


        




if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500,150))
    screen.fill(BLACK)
    canPlay = True
    clock = pygame.time.Clock()

    while canPlay:
        #TODO CATCH CONTROLS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
        #FILL 
        screen.fill(BLACK)

        #TODO UPDATE

        #DRAW
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


