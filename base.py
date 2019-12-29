import pygame
import os

baseImage=pipeImage= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","base.png" ) ) )

class Base:
    velocity=5
    width=baseImage.get_width()
    image=baseImage
    
    def __init__(self, y):
        self.y=y
        self.x1=0
        self.x2=self.width
        
    def move(self):
        self.x1-=self.velocity
        self.x2-=self.velocity
        
        if(self.x1+self.width<0):
            self.x1=self.x2+self.width
        if(self.x2+self.width<0):
            self.x2=self.x1+self.width
            
    def draw(self,window):
        window.blit(self.image,(self.x1,self.y))
        window.blit(self.image,(self.x2,self.y))