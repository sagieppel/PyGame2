import pygame 
pygame.init()

screenSize=600
screen=pygame.display.set_mode([screenSize,screenSize]) 

for i in range(100000000):
   red=255
   green=0
   blue=100
   x=200
   y=200
   scale=10
   pygame.draw.circle(screen, [red,green,blue], [x,y], scale)
   pygame.display.update()
