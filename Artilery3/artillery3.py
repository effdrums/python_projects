import pygame
import menu 
import tank


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

    tank_size = {'x':10, 'y':4}

    tank1 = tank.Tank(RED,tank_size['x'],tank_size['y'])
    tank2 = tank.Tank(GREEN,tank_size['x'],tank_size['y'])

    tank1.rect.x = 10
    tank1.rect.y = 140

    tank2.rect.x = 480
    tank2.rect.y = 140

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(tank1)
    all_sprites_list.add(tank2)

    while canPlay:
        #TODO CATCH CONTROLS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
        #FILL 
        screen.fill(BLACK)

        #TODO UPDATE

        #DRAW
        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


