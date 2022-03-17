import pygame 
import random

pygame.init()

screensize=700 
screen=pygame.display.set_mode([screensize,screensize]) # 

circle = {}
circle["color"] = [0,0,255]
circle["x"] = 100
circle["y"] = 100
circle["radius"] = 40

for i in range(1000000):
  pygame.draw.circle(screen, circle["color"], [circle["x"],circle["y"]], circle["radius"])
  pygame.display.update()
