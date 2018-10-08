import pygame

class Tank(pygame.sprite.Sprite): 

    def _init_(self, _color, _x_pos, _y_pos):
        print("Creating new Tank...")

        self.image = pygame.Surface([_x_pos,_y_pos])
        self.image.fill(_color)

        self.rect = self.image.get_rect()


    def update(self):
        print("Calling Update Tank...")

    

    

