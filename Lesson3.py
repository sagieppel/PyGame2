import pygame
import random

#-----------------Create a circle--------------------------------------------------------
def create(x,y):
  circle={}
  circle["color"]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["size"]=10#random.randint(10,100)
  circle["xspeed"]=0.1
  circle["yspeed"]=0.1
  return circle
  
#------------------Draw a circle--------------------------------------------------------
def update(circle):
    circle["x"] += circle["xspeed"]
    circle["y"] += circle["yspeed"]
    pygame.draw.circle(screen, circle["color"], [int(circle["x"]),int(circle["y"])], int(circle["size"]))

#----------------initiate pygame---------------------------------------------------------
pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize])


circle = create(300, 400)
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
    pygame.Surface.fill(screen,(0,0,0))
    update(circle)
    pygame.display.update()
    
 

