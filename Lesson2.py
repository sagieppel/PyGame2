import pygame 
import random

pygame.init()

screensize=700 
screen=pygame.display.set_mode([screensize,screensize]) # 

red=255
green=0
blue=0

x = 100
y = 100
size = 30


for i in range(10000):
  pygame.draw.circle(screen, [red,green,blue], [x,y], size)
  pygame.display.update()
