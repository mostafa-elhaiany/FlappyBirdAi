import pygame
import neat
import time
import os
import random

windowWidth,windowHeight=500,800

birdImages = [
        pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bird1.png" ) ) ),
        pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bird2.png" ) ) ),
        pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bird3.png" ) ) )
        ]
numImages=len(birdImages)
pipeImage= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","pipe.png" ) ) )

backGround= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bg.png" ) ) )

baseImage=pipeImage= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","base.png" ) ) )


class Flappy:
    images=birdImages
    maxRotation= 25 #how much the bird tilts after a jump
    rotationVelocity = 20 #how much we're going to rotate on each frame 
    animationTime = 5 #animation per second for every sprite
    
    def __init__(self,x,y): #the starting position of the bird
        self.x=x
        self.y=y
        self.tilt=0
        self.tickCount=0 
        self.velocity=0
        self.height=y
        self.imageCount=0 #which sprite of image is shoing
        self.imageNumber=0
        self.image=self.images[0]
    
    def jump(self):
        self.velocity=-10.5
        self.tickCount=0
        self.height=self.y
        
    def move(self):
        self.tickCount+=1
        
        displacement = self.velocity*self.tickCount + 1.5*(self.tickCount**2)
        if(displacement>=16):
             displacement=16
        elif(displacement<0):
            displacement-=2
            
        self.y+=displacement
        if(displacement<0 or self.y < (self.height+50) ):
            if(self.tilt<self.maxRotation):
                self.tilt=self.maxRotation
        else:
            if(self.tilt > -90):
                self.tilt -= self.rotationVelocity
                
        
    def draw(self, window):
        self.imageCount+=1
        
        if(self.imageCount%self.animationTime==0):
            self.imageNumber+=1
            self.image=self.images[self.imageNumber%numImages]
            
        if(self.tilt <=-80):
            self.image=self.images[1]
            self.imageCount=self.animationTime*2
            
            
        rotatedImage= pygame.transform.rotate(self.image,self.tilt)
        newRectangle= rotatedImage.get_rect(center=self.image.get_rect(topleft=(self.x,self.y)).center)
        window.blit(rotatedImage,newRectangle.topleft)
    
    
    def getMask(self):
        return pygame.mask.from_surface(self.image)
        

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
    
    