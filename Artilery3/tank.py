import pygame
import healthBar
import bombBar
import fuelBar
import chargeBar
import cannon
import time
import random


SELECT_ACTION = 0
REPAIR = 1
CHARGEBOMB = 2
FUEL = 3
MOVE = 4
SHOOT = 5
CHARGE = 6

class Tank(pygame.sprite.Sprite): 

    myHealthBar = None
    myBombBar = None
    myFuelBar = None
    myCannon = None
    myChargeBar = None

    active_group = None
    
    shake_count = 0
    shake_up = True
    
    time_start_shake = None
    time_start_charge = None
    min_elapsed_charge = 0.5
    min_elapsed = 0.100

    screen_size = None

    changeTurn = False
    hasShoot = False
    hasCharged = False
    hasRepared = False
    hasChargedBomb = False
    hasFueled = False


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

        self.myChargeBar = chargeBar.ChargeBar()

        self.myCannon = cannon.Cannon(_color,(10,2))

        self.active_group = pygame.sprite.Group()
        
    def setPos(self, _x_pos, _y_pos):
        self.rect.x = _x_pos
        self.rect.y = _y_pos
        self.myCannon.rect.center = (_x_pos + int(self.rect.width / 2), _y_pos)
        #self.myCannon.setPos(_x_pos , _y_pos)

    def setScreenSize(self, screen_width, screen_height):
        self.screen_size = { 'w': screen_width, 'h': screen_height }

        
    def isChangeTurn(self):
        return self.changeTurn

    def update(self,event, key, ev_type):
        print("Calling Update Tank..." + str(event))
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
            if not self.hasRepared and self.myChargeBar.has_health:
                if ev_type == pygame.KEYUP and key == pygame.K_r:
                    self.myHealthBar.restart()
                    self.myChargeBar.removeHealthCharge()
                    self.hasRepared = True
                    self.time_start_charge = time.time()
            else:
                if time.time() - self.time_start_charge > self.min_elapsed_charge:
                    print("REPARED!!")
                    self.changeTurn = True
                    self.hasRepared = False
            
        elif event == CHARGEBOMB:
            print("Using CHARGEBOMB...")
            if not self.hasChargedBomb and self.myChargeBar.has_bomb:
                if ev_type == pygame.KEYUP and key == pygame.K_b:
                    self.myBombBar.restart()
                    self.myChargeBar.removeBombCharge()
                    self.hasRepared = True
                    self.time_start_charge = time.time()
            else:
                if time.time() - self.time_start_charge > self.min_elapsed_charge:
                    self.changeTurn = True
                    self.hasChargedBomb = False

        elif event == FUEL:
            print("Charge fuel...")
            print("Repairing...")
            if not self.hasFueled and self.myChargeBar.has_fuel:
                if ev_type == pygame.KEYUP and key == pygame.K_f:
                    self.myFuelBar.restart()
                    self.myChargeBar.removeFuelCharge()
                    self.hasFueled = True
                    self.time_start_charge = time.time()
            else:
                if time.time() - self.time_start_charge > self.min_elapsed_charge:
                    print("REPARED!!")
                    self.changeTurn = True
                    self.hasFueled = False
                    
        elif event == MOVE:
            print("Move...")
            if self.myFuelBar.current_fuel > 0:
                if ev_type == pygame.KEYDOWN:
                    if key == pygame.K_RIGHT:
                        print("Moving right")
                        if (self.rect.x + self.image.get_width() < self.screen_size['w'] - self.image.get_width() ):
                            x = self.rect.x + 1
                            self.setPos(x,self.rect.y)
                            self.myFuelBar.consume()

                    elif key == pygame.K_LEFT:
                        print("Moving left")
                        if self.rect.x > 0: 
                            x = self.rect.x - 1
                            self.setPos(x, self.rect.y)
                            self.myFuelBar.consume()
                elif ev_type == pygame.KEYUP:
                    if key == pygame.K_RIGHT or key == pygame.K_LEFT:
                        print("CHANGE!!!")
                        self.changeTurn = True
            
            else:
                self.changeTurn = True
                #TODO notify user not fuel 

            
                

        elif event == SHOOT:
            print("Shooting...")
            if not self.active_group.has(self.myCannon):
                self.active_group.add(self.myCannon)
            if ev_type == pygame.KEYDOWN:
                if key == pygame.K_SPACE:
                    self.hasShoot = True
                    angle = self.myCannon.angle
                    x_init = self.myCannon.rect.centerx
                    y_init = self.myCannon.rect.centery
                    self.tankInitShoot(angle , x_init, y_init)

            if not self.hasShoot:
                self.myCannon.rotate()
            else:
                print("Shoot angle = " + str(self.myCannon.degree))
                self.active_group.remove(self.myCannon)
                self.tankShoot()
                
                if self.myBombBar.isShootFinish() :
                    self.hasShoot = False
                    self.changeTurn = True

        elif event == CHARGE:
            if not self.hasCharged:
                if ev_type == pygame.KEYUP and key == pygame.K_c:
                    print("Get random charge...")
                    rand_charge = random.randint(0,2)
                    if rand_charge == 0:
                        self.myChargeBar.addBombCharge()
                        self.myChargeBar.has_bomb =  True
                    elif rand_charge == 1:
                        self.myChargeBar.addFuelCharge()
                        self.myChargeBar.has_fuel = True
                    elif rand_charge == 2:
                        self.myChargeBar.addHealthCharge()
                        self.myChargeBar.has_health = True

                    self.hasCharged = True
                    self.time_start_charge = time.time()
            else:        
                if time.time() - self.time_start_charge > self.min_elapsed_charge:    
                    self.changeTurn = True
                    self.hasCharged = False
                



    def drawInfo(self, screen):
        self.myHealthBar.draw(screen)
        self.myBombBar.draw(screen)
        self.myFuelBar.draw(screen)
        self.myChargeBar.draw(screen)
        self.active_group.draw(screen)

    

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

    def tankInitShoot(self, angle , x_init, y_init):
        self.myBombBar.initShoot(angle, x_init, y_init)

    def tankShoot(self):
        self.myBombBar.shoot()

    def tankShootCheck(self, group_tank):
        current_bomb = self.myBombBar.getBoombShooted()
        collided = pygame.sprite.spritecollideany(current_bomb, group_tank)
        if collided and collided != self:
            self.myBombBar.setShootFinish()
            self.hasShoot = False        
            self.changeTurn = True
            return collided

    def tankLooseHealt(self):
        self.myHealthBar.loseHealth()

    def tankIsDead(self):
        if self.myHealthBar.current_life > 0:
            return False
        else:
            return True
        


