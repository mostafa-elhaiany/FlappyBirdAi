import pygame
import neat
import time
import os
from flappy import Flappy
from pipe import Pipe
from base import Base

backGround= pygame.transform.scale2x( pygame.image.load( os.path.join( "imgs","bg.png" ) ) )
windowWidth,windowHeight=500,700

pygame.font.init()

statFont=pygame.font.SysFont("comicsans",50)


def drawWindow(window,birds,pipes,base,score):
    window.blit(backGround,(0,0))
    base.draw(window)
    for pipe in pipes:
        pipe.draw(window)
    for bird in birds:
        bird.draw(window)
    text = statFont.render("Score: "+str(score),1, (255,255,255))
    window.blit(text,(windowWidth - 10 - text.get_width(), 10))
    pygame.display.update()
    

def main(genomes,config):
    #bird=Flappy(230,350)
    networks=[]
    genes=[]
    birds=[] 
    
    for _,g in genomes:
        net=neat.nn.FeedForwardNetwork.create(g,config)
        networks.append(net)
        birds.append(Flappy(230,350))
        g.fitness=0
        genes.append(g)
        
    
    base=Base(windowHeight-70)
    pipes= [Pipe(windowWidth+50)]
    score=0
    run = True
    clock=pygame.time.Clock()
    window=pygame.display.set_mode((windowWidth,windowHeight))
    while(run):
        addPipe=False
       # clock.tick(30)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
                pygame.quit()
                quit()
                
        pipeIndex=0
        if(len(birds)>0):
            if(len(pipes)>1 and birds[0].x > pipes[0].x + pipes[0].pipeTop.get_width()):
                pipeIndex=1
        else:
            run=False
            break
        for idx,bird in enumerate(birds):
            bird.move()
            genes[idx].fitness+=0.1
            
            distanceTop=abs(bird.y-pipes[pipeIndex].height)
            distanceBottom=abs(bird.y-pipes[pipeIndex].bottom)
            output=networks[idx].activate((bird.y,distanceTop,distanceBottom))
            
            if(output[0]>0.5):
                bird.jump()
            
            
        
        base.move()
        newPipes=[]
        for pipe in pipes:
            for idx,bird in enumerate(birds):
                if(pipe.collide(bird)):
                    genes[idx].fitness-=1
                    birds.pop(idx)
                    networks.pop(idx)
                    genes.pop(idx)
                if(not pipe.passed and pipe.x<bird.x):
                    pipe.passed=True
                    addPipe=True
            
            if(not pipe.x+pipe.pipeTop.get_width()<0):
                newPipes.append(pipe)
            pipe.move()
       
        if(addPipe):
            score+=1
            for g in genes:
                g.fitness+=5
            newPipes.append(Pipe(windowWidth+50))
        pipes=newPipes                
       
        for idx,bird in enumerate(birds):
            if(bird.y+bird.image.get_height()>=windowHeight or bird.y<=0):
                birds.pop(idx)
                networks.pop(idx)
                genes.pop(idx)
            
        
        drawWindow(window, birds ,pipes,base,score)

def run(configPath):
    config= neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            configPath)
    population = neat.Population(config)
    
    population.add_reporter(neat.StdOutReporter(True))
    stats=neat.StatisticsReporter()
    population.add_reporter(stats)

    winner= population.run(main,50)
    
if __name__=="__main__":
    localDirectory= os.path.dirname(__file__)
    configPath= os.path.join(localDirectory,"config.txt")
    run(configPath)


