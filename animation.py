import pygame
import math
import random
import time

pygame.init()


size = (800,600)
blue = (50, 200, 250)
green = (50, 250, 50)
white = (255, 255, 255)
black = (0, 0, 0)
crowd = pygame.transform.scale (pygame.image.load("crowd.png"),(900,200))
sun = pygame.transform.scale (pygame.image.load("sun.png"),(80,80))
rugbyball = pygame.transform.scale (pygame.image.load("rugbyball.png"),(35,20))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

ballx = 400
bally = 500
done = True
changex = 0

file = 'cheer.ogg'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)


#game loop
while done:
    
    pygame.draw.rect(screen,blue , (0,0,800,400))
    pygame.draw.rect(screen,green , (0,400,800,400))
    screen.blit(crowd,[0,250,0,0])
    screen.blit(sun,[0,20,0,200])
    pygame.draw.rect(screen,black , (250,50,12,402))
    pygame.draw.rect(screen,black , (500,50,12,402))
    pygame.draw.rect(screen,black , (250,225,252,12))
    pygame.draw.rect(screen,white , (250,50,10,400))
    pygame.draw.rect(screen,white , (500,50,10,400))
    pygame.draw.rect(screen,white , (250,225,250,10))
    ballx += changex
    bally -= 4
    screen.blit(rugbyball,[ballx,bally,0,200])
    
    if bally < 0:
        ballx = 400
        bally = 500
        changex = random.uniform(-5,5)
        pygame.mixer.music.stop()

    if bally < 225 and ballx > 255 and ballx < 475:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        
        
    #update
    pygame.display.flip()
    clock.tick(50)

    

    

    
