import pygame
import menu 
import tank
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

tank_colors = [WHITE, BLUE, GREEN, RED]

        

 


if __name__ == "__main__":

    myMenu = menu.MenuArtillery3()

    myMenu.run()

    pygame.init()
    screen_width = 500
    screen_height = 150
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(BLACK)
    canPlay = True
    clock = pygame.time.Clock()

    canPlay = myMenu.start_game

    tank_sprites_list = pygame.sprite.Group()
    tank_size = {'x':10, 'y':4}

    color_index = random.randint(0,3)
    print(color_index)

    for i in range(myMenu.num_max_tanks):
        print(i)
        index = (color_index + i) % len(tank_colors)
        tank_aux = tank.Tank(tank_colors[index],tank_size['x'],tank_size['y'])
        tank_aux.rect.x = random.randrange(10, screen_width - 20)
        tank_aux.rect.y = screen_height - 10
        tank_sprites_list.add(tank_aux)


    while canPlay:
        #TODO CATCH CONTROLS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
        #FILL 
        screen.fill(BLACK)

        #TODO UPDATE

        #DRAW
        tank_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


