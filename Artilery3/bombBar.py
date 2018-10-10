import pygame

GRAY = (105,105,105)

class BombBlock(pygame.sprite.Sprite):

    def __init__(self,_color, _radius):
        super().__init__()

        self.image = pygame.Surface([2*_radius,2*_radius])
        #self.image.fill(_color)

        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, GRAY,(_radius,_radius), _radius)

    def setPos(self,_x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos


        

class BombBar:

    max_bomb = 3
    bomb_sprite_list = None
    block_size = 3
    offset = 2 

    def __init__(self):
        self.bomb_sprite_list = pygame.sprite.Group()
        for i in range(self.max_bomb):
            self.bomb_sprite_list.add(BombBlock(GRAY,self.block_size))

        
    def setPos(self, _x_pos, _y_pos):
        bomb_sprites = self.bomb_sprite_list.sprites()
        
        for i in range(self.max_bomb):
            bomb_sprites[i].setPos(_x_pos + (i*(2*self.block_size + self.offset)), _y_pos)
    
    def draw(self,screen):
        self.bomb_sprite_list.draw(screen)
    
    def getGroup(self):
        return self.bomb_sprite_list