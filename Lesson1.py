import pygame 
import random

pygame.init()

screenSize=600
screen=pygame.display.set_mode([screenSize,screenSize]) 

for i in range(100000000):
   pygame.event.get()
   x,y = pygame.mouse.get_pos()
   red=random.randint(0,255)
   green=random.randint(0,255)
   blue=random.randint(0,255)
  # x=random.randint(0,600)
  # y=random.randint(0,600)
   scale=random.randint(0,55)
   pygame.draw.circle(screen, [red,green,blue], [x,y], scale)
   pygame.display.update()
   
   
