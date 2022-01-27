import pygame
import random
#-----------------Create a circle--------------------------------------------------------
def create(x,y):
  circle={}
  circle["color"]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["size"]=10#random.randint(10,100)
  return circle
#------------------Draw a circle--------------------------------------------------------
def update(circle):
    pygame.draw.circle(screen, circle["color"], [int(circle["x"]),int(circle["y"])], int(circle["size"]))
#----------------initiate pygame---------------------------------------------------------
pygame.init()
screensize=500
screen=pygame.display.set_mode([screensize,screensize])

circle = create(200, 200)
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
    update(circle)
    pygame.display.update()
    
  
  
  
#   pygame.event.get()
#   x,y = pygame.mouse.get_pos() # Get position of the mouse
  
#   pygame.Surface.fill(screen,(0,0,0))
 

