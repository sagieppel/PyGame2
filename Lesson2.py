import pygame 
import random

###############################################################################3
def createCircle(x,y):
   circle = {}
   
   
   circle["red"]=random.randint(0,255)
   circle["green"]=random.randint(0,255)
   circle["blue"]=random.randint(0,255)
   
   circle['x']=x#+random.randint(-50,50)
   circle['y']=y#+random.randint(-50,50)
   
   circle["scale"]= 20# random.randint(0,5)
   #pygame.time.delay(5)
   
   pygame.draw.circle(screen, [circle["red"], circle["green"], circle["blue"]], [circle['x'],circle['y']], circle["scale"])
   pygame.display.update()
###############################################################################

pygame.init()

screenSize=700
screen=pygame.display.set_mode([screenSize,screenSize]) 


for i in range(100000000):
   pygame.event.get()
   x,y = pygame.mouse.get_pos()
   createCircle(x,y)
   createCircle(100,100)
   createCircle(300,300)
