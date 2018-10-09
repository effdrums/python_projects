import pygame

import healthBar


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


if __name__ == "__main__":
    pygame.init()
    screen_width = 500
    screen_height = 150
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(BLACK)
    canPlay = True
    clock = pygame.time.Clock()

    myHealthBar = healthBar.HealthBar()
    myHealthBar.setPos(2,2)

    while canPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
            elif event.type == pygame.KEYDOWN:
                key_event = event.key
                print("Event key= " + event.unicode)

            myHealthBar.getGroup().draw(screen)

            pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()