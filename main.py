import pygame
import neat
import time
import os
import random
from flappy import Flappy
from pipe import Pipe

backGround= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bg.png" ) ) )
windowWidth,windowHeight=500,800




def drawWindow(window,bird):
    window.blit(backGround,(0,0))
    bird.draw(window)
    pygame.display.update()
    

def main():
    bird=Flappy(200,200)
    run = True
    clock=pygame.time.Clock()
    window=pygame.display.set_mode((windowWidth,windowHeight))
    while(run):
        clock.tick(30)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
        bird.move()
        drawWindow(window, bird)
    pygame.quit()
    quit()          
    
main()