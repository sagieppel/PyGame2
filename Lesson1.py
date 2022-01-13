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
   x=x+random.randint(-50,50)
   y=y+random.randint(-50,50)
   scale=random.randint(0,5)
   pygame.time.delay(5)
   pygame.draw.circle(screen, [red,green,blue], [x,y], scale)
   pygame.display.update()
   
   
