import pygame 
import random

pygame.init()

screensize=700 
screen=pygame.display.set_mode([screensize,screensize]) # 

circle = {}
circle["color"] = [0,0,255]
circle['x'] = 200
circle['y'] = 100
circle["radius"] = 40
circle["speedX"] = 1
circle["speedY"] = -1

for i in range(1000000):
  screen.fill((0,0,0))
  circle['x'] = circle['x'] + circle["speedX"]
  pygame.draw.circle(screen, circle["color"], [circle['x'],circle['y']], circle["radius"])
  pygame.display.update()
