import pygame

SELECT_ACTION = 0
REPAIR = 1
SHIELD = 2
FUEL = 3
MOVE = 4
SHOOT = 5
CHARGE = 6

class Tank(pygame.sprite.Sprite): 


    def __init__(self, _color, _x_pos, _y_pos):
        print("Creating new Tank...")

        super().__init__()

        self.image = pygame.Surface([_x_pos,_y_pos])
        self.image.fill(_color)

        self.rect = self.image.get_rect()


    def update(self,event, key):
        print("Calling Update Tank...")
        if event == SELECT_ACTION:
            print("Selecting Action...")
        elif event == REPAIR:
            print("Repairing...")
        elif event == SHIELD:
            print("Using shield...")
        elif event == FUEL:
            print("Charge fuel...")
        elif event == MOVE:
            print("Move...")
        elif event == SHOOT:
            print("Shooting...")
        elif event == CHARGE:
            print("Get random charge...")



