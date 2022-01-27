import pygame
import random

#-----------------Create a circle--------------------------------------------------------
def create(x,y):
  circle={}
  circle["color"]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["size"]= random.randint(1,10)
  circle["xspeed"]=random.randint(-100,100)/1000
  circle["yspeed"]=random.randint(-100,100)/1000
  circle["noise"]=0.01
  return circle
  
#------------------Draw a circle--------------------------------------------------------
def update(circle):
    circle["x"] +=  circle["xspeed"]+random.randint(-100,100)*circle["noise"]
    circle["y"] += circle["yspeed"]+random.randint(-100,100)*circle["noise"]
    pygame.draw.circle(screen, circle["color"], [int(circle["x"]),int(circle["y"])], int(circle["size"]))

#----------------initiate pygame---------------------------------------------------------
pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize])
ar=[]
for i in range(100):
     circle = create(200, 200)
     ar.append(circle)
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
    pygame.Surface.fill(screen,(0,0,0))
    for circle in ar:
        update(circle)
    pygame.display.update()
    
 

