import pygame
import healthBar
import bombBar
import fuelBar
import time

SELECT_ACTION = 0
REPAIR = 1
SHIELD = 2
FUEL = 3
MOVE = 4
SHOOT = 5
CHARGE = 6

class Tank(pygame.sprite.Sprite): 

    myHealthBar = None
    myBombBar = None
    myFuelBar = None
    
    shake_count = 0
    shake_up = True
    
    time_start_shake = None
    min_elapsed = 0.100

    screen_size = None

    changeTurn = False


    def __init__(self, _color, _width, _height):
        print("Creating new Tank...")

        super().__init__()

        self.image = pygame.Surface([_width,_height])
        self.image.fill(_color)

        self.rect = self.image.get_rect()

        self.myHealthBar = healthBar.HealthBar()
        self.myHealthBar.setPos(2,2)
        
        self.myBombBar = bombBar.BombBar()
        self.myBombBar.setPos(2,10)

        self.myFuelBar = fuelBar.FuelBar()
        self.myFuelBar.setPos(2,20)

    def setPos(self, _x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos

    def setScreenSize(self, screen_width, screen_height):
        self.screen_size = { 'w': screen_width, 'h': screen_height }

        
    def isChangeTurn(self):
        return self.changeTurn

    def update(self,event, key, ev_type):
        #print("Calling Update Tank..." + str(event))
        if self.time_start_shake is None:
            self.time_start_shake = time.time()

        if (time.time() - self.time_start_shake) >= self.min_elapsed:
            self.tankShake()

        if event == SELECT_ACTION:
            #print("Selecting Action...")
            
            if self.time_start_shake is None:
                self.time_start_shake = time.time()

            if (time.time() - self.time_start_shake) >= self.min_elapsed:
                self.tankShake()

        elif event == REPAIR:
            print("Repairing...")
        elif event == SHIELD:
            print("Using shield...")
        elif event == FUEL:
            print("Charge fuel...")
        elif event == MOVE:
            print("Move...")
            if ev_type == pygame.KEYDOWN:
                if key == pygame.K_RIGHT:
                    print("Moving right")
                    if (self.rect.x + self.image.get_width() < self.screen_size['w'] - self.image.get_width() ):
                        self.rect.x += 1
                        self.myFuelBar.consume()
                        
                elif key == pygame.K_LEFT:
                    print("Moving left")
                    if self.rect.x > 0: 
                        self.rect.x -= 1
                        self.myFuelBar.consume()
            elif ev_type == pygame.KEYUP:
                if key == pygame.K_RIGHT or key == pygame.K_LEFT:
                    print("CHANGE!!!")
                    self.changeTurn = True

            
                

        elif event == SHOOT:
            print("Shooting...")
        elif event == CHARGE:
            print("Get random charge...")


    def drawInfo(self, screen):
        self.myHealthBar.getGroup().draw(screen)
        self.myBombBar.getGroup().draw(screen)
        self.myFuelBar.getGroup().draw(screen)

    def tankShake(self):
        self.time_start_shake = time.time()
        max_shake = 2
        min_shake = 0  
        if self.shake_up:
            self.rect.y -= 1
            self.shake_count += 1
            if self.shake_count == max_shake:
                self.shake_up = False
        elif not self.shake_up:
            self.rect.y += 1
            self.shake_count -= 1
            if self.shake_count == 0:
                self.shake_up = True



