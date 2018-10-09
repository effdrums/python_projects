import pygame
import menu 
import tank
import random

#DEFINE EVENTS
SELECT_ACTION = 0
REPAIR = 1
SHIELD = 2
FUEL = 3
MOVE = 4
SHOOT = 5
CHARGE = 6

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

    current_player = random.randint(0,2)

    key_event = None
    current_event = SELECT_ACTION
    next_event = None

    while canPlay:
        #TODO CATCH CONTROLS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
            elif event.type == pygame.KEYDOWN:
                key_event = event.key
                print("Event key= " + event.unicode)
                                
        #FILL 
        #screen.fill(BLACK)

        #TODO UPDATE
        if current_event == SELECT_ACTION:
            if key_event == pygame.K_s:
                next_event = SHOOT
            if key_event == pygame.K_r:
                next_event = REPAIR
            if key_event == pygame.K_a:
                next_event = SHIELD
            if key_event == pygame.K_f:
                next_event = FUEL
            if key_event == pygame.K_m:
                next_event = MOVE
            if key_event == pygame.K_c:
                next_event = CHARGE
                

            tank_sprites_list.sprites()[current_player].update(next_event, key_event)

        #DRAW
        #tank_sprites_list.draw(screen)

        #pygame.display.flip()

        clock.tick(60)

    pygame.quit()


