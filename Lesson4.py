import pygame
import random

#-----------------Create a circle--------------------------------------------------------
def create(x,y):
  circle={}
  circle["color"]=[255, 255, 255] # [Red,Green,Blue]
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["size"]= random.randint(10,40)
  circle["xspeed"]=0#random.randint(-100,100)/1000
  circle["yspeed"]=0#random.randint(-100,100)/1000
  circle["noise"]=0.005
  return circle
  
#------------------Draw a circle--------------------------------------------------------
def update(circle):
    circle["x"] +=  circle["xspeed"]+random.randint(-100,100)*circle["noise"]
    circle["y"] += circle["yspeed"]+random.randint(-100,100)*circle["noise"]
    if random.randint(0,1000)==1:
          circle["color"]=[0, 0, 255]
          circle["yspeed"]= 1
          circle["size"] = 2
          
      
    pygame.draw.circle(screen, circle["color"], [int(circle["x"]),int(circle["y"])], int(circle["size"]))

#----------------initiate pygame---------------------------------------------------------
pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize])
#---------------Create cloud array------------------------------
ar=[] # Create array
for i in range(400):
     circle = create(random.randint(100,200), random.randint(100,200))
     ar.append(circle)
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
    
    ev=pygame.event.get()
    x,y = pygame.mouse.get_pos()

    pygame.Surface.fill(screen,(0,0,0))
    for circle in ar:
        update(circle)
    pygame.display.update()
