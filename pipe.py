import pygame
import os
import random

pipeImage= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","pipe.png" ) ) )

class Pipe:
    gap=200
    velocity=5
    
    
    def __init__(self,x):
        self.x=x
        self.height=0
        self.top=0
        self.bottom=0
        self.pipeTop=pygame.transform.flip(pipeImage,False,True)
        self.pipeBottom = pipeImage
        
        self.passed=False
        
        self.setHeight()
        
    def setHeight(self):
        self.height= random.randrange(50,450)
        self.top= self.height - self.pipeTop.get_height()
        self.bottom = self.height+self.gap
        
        
    def move(self):
        self.x-=self.velocity
        
    
    def draw(self, window):
        window.blit(self.pipeTop,(self.x,self.top))
        window.blit(self.pipeBottom,(self.x,self.bottom))
        
    def getMask(self):
        return pygame.mask.from_surface(self.pipeTop),pygame.mask.from_surface(self.pipeBottom)
        
    def collide(self,bird):
        birdMask=bird.getMask()
        topMask,bottomMask= self.getMask()
        
        topOffset = ( self.x-bird.x , self.top - round(bird.y) )
        bottomOffset = ( self.x-bird.x , self.bottom - round(bird.y) )
        
        bottomPoint=birdMask.overlap(bottomMask,bottomOffset)
        topPoint=birdMask.overlap(topMask,topOffset)
        
        if(topPoint or bottomPoint):
            return True
        
        return False
        
 