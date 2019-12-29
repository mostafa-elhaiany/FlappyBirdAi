import pygame
import neat
import time
import os
from flappy import Flappy
from pipe import Pipe
from base import Base

backGround= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bg.png" ) ) )
windowWidth,windowHeight=500,700




def drawWindow(window,bird,pipes,base):
    window.blit(backGround,(0,0))
    bird.draw(window)
    base.draw(window)
    for pipe in pipes:
        pipe.draw(window)
    pygame.display.update()
    

def main():
    bird=Flappy(230,350)
    base=Base(windowHeight-70)
    pipes= [Pipe(windowWidth+10)]
    score=0
    run = True
    clock=pygame.time.Clock()
    window=pygame.display.set_mode((windowWidth,windowHeight))
    while(run):
        addPipe=False
        clock.tick(30)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
        #bird.move()
        base.move()
        newPipes=[]
        for pipe in pipes:
            if(pipe.collide(bird)):
                print("ouch")
            
            if(not pipe.x+pipe.pipeTop.get_width()<0):
                newPipes.append(pipe)
            if(not pipe.passed and pipe.x<bird.x):
                pipe.passed=True
                addPipe=True
            pipe.move()
       
        if(addPipe):
            score+=1
            newPipes.append(Pipe(windowWidth+10))
        pipes=newPipes                
        drawWindow(window, bird,pipes,base)
    pygame.quit()
    quit()          
    
main()