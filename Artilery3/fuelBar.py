import pygame


BLUE = (0, 0, 255)

class FuelBlock(pygame.sprite.Sprite):

    def __init__(self,_color, _width, _height):
        super().__init__()

        self.image = pygame.Surface([_width,_height])
        self.image.fill(_color)

        self.rect = self.image.get_rect()


    def setPos(self,_x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos

    

class FuelBar:

    max_fuel = 100
    fuel_sprite_list = None
    block_size = {'x':68, 'y':5}
    block_pos = None
    current_fuel = 100 

    def __init__(self):
        self.fuel_sprite_list = pygame.sprite.Group()
        
        self.fuel_sprite_list.add(FuelBlock(BLUE,self.block_size['x'],self.block_size['y']))

        
    def setPos(self, _x_pos, _y_pos):
        fuel_sprites = self.fuel_sprite_list.sprites()      
        fuel_sprites[0].setPos(_x_pos, _y_pos)
        self.block_pos = {'x':_x_pos,'y':_y_pos}

    def draw(self,screen):
        self.fuel_sprite_list.draw(screen)
    
    
    def getGroup(self):
        return self.fuel_sprite_list

    def consume(self):
        print("CONSUME")
        if self.current_fuel > 0:
            
            self.current_fuel -= 0.2
            
            if self.current_fuel <0: 
                self.current_fuel = 0
            
            new_width = int( int(self.current_fuel) * self.block_size['x'] / self.max_fuel)
            print(new_width)
            sprite = self.fuel_sprite_list.sprites()[0]
            sprite.image = pygame.transform.scale(sprite.image, (new_width, self.block_size['y']))
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = self.block_pos['x']
            sprite.rect.y = self.block_pos['y']