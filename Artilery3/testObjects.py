import pygame

import healthBar
import bombBar
import fuelBar
import cannon
import chargeBar


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


if __name__ == "__main__":
    pygame.init()
    screen_width = 500
    screen_height = 150
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(BLACK)
    canPlay = True
    clock = pygame.time.Clock()

    myHealthBar = healthBar.HealthBar()
    myBombBar = bombBar.BombBar()
    myFuelBar = fuelBar.FuelBar()
    myChargeBar = chargeBar.chargeBar()
    myChargeBar.addHealthCharge()
    myChargeBar.addBombCharge()
    myChargeBar.addFuelCharge()

    myCannon = cannon.Cannon(GREEN, (10,2))
    myCannon.setPos(100,100)

    group = pygame.sprite.Group()
    group.add(myCannon)
    
    myHealthBar.setPos(2,2)
    myBombBar.setPos(2,10)
    myFuelBar.setPos(2,20)
    hasShoot = False

    while canPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                canPlay = False
            elif event.type == pygame.KEYDOWN:
                key_event = event.key
                print("Event key= " + event.unicode)
                #myCannon.rotate()
                hasShoot = True
                #myBombBar.initShoot(70,10,140)
                myChargeBar.removeHealthCharge()

        screen.fill(BLACK)


        if hasShoot:
            myBombBar.shoot()
        #myCannon.rotate()
        myHealthBar.draw(screen)
        myBombBar.draw(screen)
        myFuelBar.draw(screen)
        myChargeBar.draw(screen)
        group.draw(screen)
            
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()