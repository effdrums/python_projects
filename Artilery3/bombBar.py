import pygame
import math

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

    x_bomb = 30
    y_bomb = 30
    x_bomb_init = 0
    y_bomb_init = 0
    gravity=9.81
    angle = 0
    velocity=50
    vx=velocity * math.cos(math.radians(angle))
    vy=velocity * math.sin(math.radians(angle))
    t=0

    finish_shoot = False

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

    def getSize(self):
        print(len(self.bomb_sprite_list.sprites()))
        return len(self.bomb_sprite_list.sprites()) 
   

    def initShoot(self,angle, x_init, y_init):
        print("Init shoot")
        self.x_bomb = self.x_bomb_init = x_init
        self.y_bomb = self.y_bomb_init = y_init
        self.vx=self.velocity * math.cos(math.radians(angle))
        self.vy=self.velocity * math.sin(math.radians(angle))
        self.finish_shoot = False
        
        
    def shoot(self):
        print("Update shoot")
        if self.getSize() > 0:
            self.t +=0.1
            self.x_bomb = self.x_bomb_init + self.vx*self.t
            self.y_bomb = self.y_bomb_init - (self.vy*self.t - (self.gravity/2)*self.t*self.t)
            print("["+str(self.vy*self.t)+","+str((self.gravity/2)*self.t*self.t)+"]")
            print("["+str(self.x_bomb)+","+str(self.y_bomb)+"]")
            sprite = self.getGroup().sprites()[self.getSize()-1]
            sprite.setPos(self.x_bomb,self.y_bomb)

            if self.y_bomb > self.y_bomb_init + 30:
                self.finish_shoot = True
                self.t = 0
                self.getGroup().remove(sprite)
        else:
            self.finish_shoot = True



    def isShootFinish(self):
        return self.finish_shoot