import pygame 
import random

pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size 

red=255
blue=0
green=0
x = 100
y = 100
size = 30

for i in range(100000000):
  
  pygame.draw.circle(screen, [red,green,blue], [x,y], size)
 
  pygame.display.update()
   





pygame.init()

screenSize=700
screen=pygame.display.set_mode([screenSize,screenSize]) 


for i in range(100000000):
   pygame.event.get()
   x,y = pygame.mouse.get_pos()
   createCircle(x,y)
