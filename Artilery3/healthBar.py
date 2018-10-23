import pygame


GREEN = (0, 255, 0)

class HealthBlock(pygame.sprite.Sprite):

    def __init__(self,_color, _width, _height):
        super().__init__()

        self.image = pygame.Surface([_width,_height])
        self.image.fill(_color)

        self.rect = self.image.get_rect()

    def setPos(self,_x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos

class HealthBar:

    max_life = 10
    current_life = 10
    health_sprite_list = None
    block_size = {'x':5, 'y':5}
    offset = 2 

    def __init__(self):
        self.health_sprite_list = pygame.sprite.Group()
        for i in range(self.max_life):
            self.health_sprite_list.add(HealthBlock(GREEN,self.block_size['x'],self.block_size['y']))

        
    def setPos(self, _x_pos, _y_pos):
        health_sprites = self.health_sprite_list.sprites()
        
        for i in range(self.max_life):
            health_sprites[i].setPos(_x_pos + (i*(self.block_size['x'] + self.offset)), _y_pos)
    
    
    def draw(self,screen):
        self.health_sprite_list.draw(screen)
    
    def getGroup(self):
        return self.health_sprite_list

    def loseHealth(self):
        if self.current_life > 0:
            health_sprites = self.health_sprite_list.sprites()
            remove1 = health_sprites[self.current_life - 1]
            remove2 = health_sprites[self.current_life - 2]
            self.current_life -= 2
            self.health_sprite_list.remove(remove1)
            self.health_sprite_list.remove(remove2)


        