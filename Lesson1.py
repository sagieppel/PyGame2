import pygame 

pygame.init()

screen=pygame.display.set_mode([500,500]) # create screen

for i in range(100000):
   pygame.draw.circle(screen, [0,255,0], [200,200], 20)
   pygame.display.update()
