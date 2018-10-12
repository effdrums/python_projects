import pygame

class Cannon(pygame.sprite.Sprite):
    
    degree = 0

    def __init__(self, _color, _size):
        super().__init__()
        
        max_size = 2*max(_size[0],_size[1])
        self.original_image = pygame.Surface([max_size,max_size])
        c_draw_x_1 = int(max_size/2)
        c_draw_y_1 = int(max_size/2) - int(_size[1]/2)
        

        pygame.draw.rect(self.original_image,_color, [c_draw_x_1, c_draw_y_1, _size[0], _size[1]])
        
        self.image = self.original_image 
        
        self.rect = self.image.get_rect()

    def setPos(self,_x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos

    def rotate(self):
        print("rotate")
        self.degree += 2
        self.degree = self.degree % 360
        angle = self.degree

        if self.degree >= 180: 
            angle = - self.degree

        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image,angle)
        self.rect = self.image.get_rect()
        self.rect.center = center